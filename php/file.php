<?php

class File
{
    var $file = "";
    var $size = 0;

    function __construct($path, $size)
    {
        $this->file = $path;
        $this->size = $size;
    }
}