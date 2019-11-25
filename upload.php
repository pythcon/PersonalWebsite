<?php
    session_start();
    include('functions.php');
    include('account.php');
    gatekeeper();

    $type = filter_input(INPUT_POST, 'function', FILTER_SANITIZE_SPECIAL_CHARS);
    if ($type == "resume"){
        uploadFile($type, "resume");
    }else if ($type == "project"){
        $name           = filter_input(INPUT_POST, 'projectName', FILTER_SANITIZE_SPECIAL_CHARS);
        $description    = filter_input(INPUT_POST, 'projectDescription', FILTER_SANITIZE_SPECIAL_CHARS);
        $category    = filter_input(INPUT_POST, 'projectCategory', FILTER_SANITIZE_SPECIAL_CHARS);
        $link           = filter_input(INPUT_POST, 'projectLink', FILTER_SANITIZE_SPECIAL_CHARS);
        $image          = filter_input(INPUT_POST, 'projectImage', FILTER_SANITIZE_SPECIAL_CHARS);
        
        if ($category == ""){
            die("Please select a category.");
        }
        
        //create project directory
        mkdir("projects/".$name."/", 0744);
        addProject($name, $description, $category, $link, $image);
    }else{
        die ("Type error.");
    }
    
    echo "done";

?>
