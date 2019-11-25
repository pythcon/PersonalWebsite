<?php 
    session_start();
    include('functions.php');
    include('account.php');
    gatekeeper();

    $projectToRemove = filter_input(INPUT_POST, 'projectsList', FILTER_SANITIZE_SPECIAL_CHARS);

    if ($projectToRemove == ""){
        die("Please select a project.");
    }

    removeProject($projectToRemove);

    echo"
        <script>
            alert(\"Project removed.\");
            window.location.replace(\"/dashboard.php\");
        </script>";
?>