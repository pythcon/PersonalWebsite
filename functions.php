<?php
include('account.php');
//PHP FUNCTIONS

function redirect($targetfile){
    global $db;

    header("refresh: 0, url = $targetfile");

    exit();
}
    
function gatekeeper(){
    //check if authenticated
    if (!$_SESSION['logged']){
        echo"
        <script>
            alert(\"Not logged in...\");
            window.location.replace(\"/index.html\");
        </script>";
        exit();
    }
}

function authenticate($user, $pass){
    global $db_hostname;
    global $db_username;
    global $db_password;
    global $db_project;
    $dsn = "mysql:host=$db_hostname;dbname=$db_project";
    try {
        $db = new PDO($dsn, $db_username, $db_password);
        $sql = "SELECT * FROM login WHERE username='$user' AND password='$pass'";
        $q = $db->prepare($sql);
        $q->execute();
        $results = $q->fetchAll();

        if($q->rowCount() > 0){
            return true;
        }else{
            return false;
        } 
        $q->closeCursor();


    } catch(PDOException $e) {
        echo "Connection failed: " . $e->getMessage();
        exit();
    }
}

function uploadFile($type, $name, &$fileName){
    if ($type == "resume"){
        $file = $_FILES["resumeToUpload"];
        $target_dir = "documents/";
        $target_file = $target_dir . "ToddMurphySimpleResume.pdf";
    }else if ($type == "project"){
        $file = $_FILES["projectImage"];
        $target_dir = "projects/$name/";
        $target_file = $target_dir . basename($file["name"]);
    }else{
        die("Type Error.");
    }

    $uploadOk = 1;
    $imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

    // if everything is ok, try to upload file
    if (move_uploaded_file($file["tmp_name"], $target_file)) {
        echo "The file ". basename( $file ). " has been uploaded.";
        echo"
        <script>
            alert(\"The file ". basename($file)." has been uploaded."\");
            window.location.replace(\"/dashboard.php\");
        </script>";
        $fileName = $target_file;
    } else {
        echo "Sorry, there was an error uploading your file.";
    }
}

function addProject($name, $description, $link){
    global $db_hostname;
    global $db_username;
    global $db_password;
    global $db_project;
    
    //upload file
    uploadFile("project", $name, $fileName);
    
    $dsn = "mysql:host=$db_hostname;dbname=$db_project";
    try {
        $db = new PDO($dsn, $db_username, $db_password);
        $sql = "INSERT INTO projects VALUES ('$name','$description','$link','$fileName')";
        $q = $db->prepare($sql);

        if($q->execute() === false){
            die('Error inserting the department.');
        }
        
        $q->closeCursor();


    } catch(PDOException $e) {
        echo "Connection failed: " . $e->getMessage();
        exit();
    }
    
}


?>