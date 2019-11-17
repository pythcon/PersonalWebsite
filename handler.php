<?php

include('account.php');
include('functions.php');

$user = filter_input(INPUT_POST, 'user', FILTER_SANITIZE_SPECIAL_CHARS, FILTER_REQUIRE_ARRAY);

$pass = filter_input(INPUT_POST, 'pass', FILTER_SANITIZE_SPECIAL_CHARS, FILTER_REQUIRE_ARRAY);



?>