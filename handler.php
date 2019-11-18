<?php
session_start();
error_reporting(E_ERROR | E_WARNING | E_PARSE | E_NOTICE);
ini_set('display_errors' , 1);

include('account.php');
include('functions.php');

$user = filter_input(INPUT_POST, 'user', FILTER_SANITIZE_SPECIAL_CHARS, FILTER_REQUIRE_ARRAY);

$pass = filter_input(INPUT_POST, 'pass', FILTER_SANITIZE_SPECIAL_CHARS, FILTER_REQUIRE_ARRAY);

if (!authenticate($user, $pass)){
    redirect("<span style=\"color:red;\">Incorrect Credentials...Redirecting...</span>", "/index.html", $delay);
    die();
}

//Passed all checks
$_SESSION['logged'] = true;

redirect('dashboard.php');



?>