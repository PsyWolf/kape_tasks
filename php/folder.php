<?php
require_once('file.php');

class Folder
{
    var $location = "";
    var $totalSize = 0;
    var $totalItems = 0;
    var $files = array();

    function __construct($name, $size, $count)
    {
        $this->location = $name;
        $this->totalSize = $size;
        $this->totalItems = $count;
    }
}