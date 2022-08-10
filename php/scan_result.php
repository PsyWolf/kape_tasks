<?php
require_once('folder.php');
require_once('sort_options.php');

class Results
{
    var $folders = array();
}

class MainObj
{
    var $type = "";
    var $totalSize = 0;
    var $totalItems = 0;
    var $results = null;

    function __construct()
    {
        $this->results = new Results();
    }
}

function alphaNumericCmp($property)
{
    return fn ($a, $b) => strcmp($a->$property, $b->$property);
}

function sizeCmp($property)
{
    return fn ($a, $b) => $a->$property - $b->$property;
}


class ScanResults
{
    public function parseXML(string $xml_str, SortOptions $options)
    {
        $cmpFolder = null;
        $cmpFile = null;
        switch ($options) {
            case SortOptions::AlphaNumericSort:
                $cmpFolder = alphaNumericCmp("location");
                $cmpFile = alphaNumericCmp("file");
                break;
            case SortOptions::SizeSort:
                $cmpFolder = sizeCmp("totalSize");
                $cmpFile = sizeCmp("size");
                break;
            default:
                // leave unordered
                break;
        }
        // add xml validation
        $xml = simplexml_load_string($xml_str);
        if ($xml === false) {
            $msg = "Failed loading XML: ";
            foreach (libxml_get_errors() as $error) {
                $msg .= "\n " . $error->message;
            }
            return $msg;
        }
        $main_obj = new MainObj();
        $main_obj->type = $this->xml_attribute($xml, "type");
        if (!$main_obj->type || ($main_obj->type != "junk" && $main_obj->type != "privacy")) {
            $msg = "XML is invalid";
            return $msg;
        }
        foreach ($xml->children() as $dir) {
            $name = $this->xml_attribute($dir, "name");
            $size = $this->xml_attribute($dir, "sizeBytes");
            $count = $this->xml_attribute($dir, "items");
            if (!$name || !$size || !$count || !is_numeric($size) || !is_numeric($count)) {
                $msg = "XML is invalid";
                return $msg;
            }
            $size = (int)$size;
            $count = (int)$count;
            $folder = new Folder($name, $size, $count);
            $main_obj->totalSize += $size;
            $main_obj->totalItems += $count;

            foreach ($dir->children() as $file) {
                $path = $this->xml_attribute($file, "path");
                $size = $this->xml_attribute($file, "sizeBytes");
                if (!$path || !$size || !is_numeric($size)) {
                    $msg = "XML is invalid";
                    return $msg;
                }
                $size = (int)$size;
                $file = new File($path, $size);
                array_push($folder->files, $file);
            }
            if ($cmpFile != null) {
                usort($folder->files, $cmpFile);
            }
            array_push($main_obj->results->folders, $folder);
            if ($cmpFolder != null) {
                usort($main_obj->results->folders, $cmpFolder);
            }
        }

        return $main_obj;
    }

    public function xml_attribute($object, $attribute)
    {
        if (isset($object[$attribute]))
            return (string) $object[$attribute];
        else
            return null;
    }
}

$scan_results = new ScanResults();
$xml = '<ScanResults type="junk">
 <dir name="c:\windows\temp" items="asd" sizeBytes="2343">
 <file path="c:\windows\temp\2.file" sizeBytes="2300"/>
 <file path="c:\windows\temp\1.file" sizeBytes="43"/>
 </dir>
 <dir name="c:\user\temp" items="3" sizeBytes="32324">
 <file path="c:\user\temp\3.file" sizeBytes="6443"/>
 <file path="c:\user\temp\2.file" sizeBytes="25858"/>
 <file path="c:\user\temp\1.file" sizeBytes="23"/>
 </dir>
</ScanResults>
';

$obj = $scan_results->parseXML($xml, SortOptions::SizeSort);

echo json_encode($obj);