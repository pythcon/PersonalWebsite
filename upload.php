<?php
    session_start();
    include('functions.php');
    include('account.php');
    error_reporting(E_ERROR | E_WARNING | E_PARSE | E_NOTICE);
    ini_set('display_errors' , 1);
    gatekeeper();

    $type = filter_input(INPUT_POST, 'function', FILTER_SANITIZE_SPECIAL_CHARS);
    if ($type == "resume"){
        uploadFile($type, "resume");
    }else if ($type == "project"){
        $name           = filter_input(INPUT_POST, 'projectName', FILTER_SANITIZE_SPECIAL_CHARS);
        $description    = filter_input(INPUT_POST, 'projectDescription', FILTER_SANITIZE_SPECIAL_CHARS);
        $link           = filter_input(INPUT_POST, 'projectLink', FILTER_SANITIZE_SPECIAL_CHARS);
        $image          = filter_input(INPUT_POST, 'projectImage', FILTER_SANITIZE_SPECIAL_CHARS);
        
        //create project directory
        mkdir("projects/".$name."/", 0744);
        addProject($name, $description, $link, $image);
    }else{
        die ("Type error.");
    }
    
    echo "done";

?>
