<?php
    sleep (2.5);
    $url = "https://api.github.com/users/tmurphy605/repos"; 
    $fp = fopen ( $url , "r" ); 
    $contents = "";
    while ( $more = fread ( $fp, 1000  ) ) {      $contents .=  $more ;   }
    echo $contents ;  
?>