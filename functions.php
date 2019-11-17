<?php
include('account.php');
//PHP FUNCTIONS

function redirect($targetfile){
    global $db;

    header("refresh: 0, url = $targetfile");

    exit();
}
    
function gatekeeper(){
    global $db;
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
    $dsn = "mysql:host=$db_hostname;dbname=$db_project";
    try {
        $db = new PDO($dsn, $db_username, $db_password);
        echo "Connected successfully<br>";
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


?>