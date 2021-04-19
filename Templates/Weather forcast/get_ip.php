<?php
if (!empty($_SERVER['HTTP_CLIENT_IP']))
    {
      $ip_address = $_SERVER['HTTP_CLIENT_IP']."\r\n";
    }
elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR']))
    {
      $ip_address = $_SERVER['HTTP_X_FORWARDED_FOR']."\r\n";
    }
else 
    {
      $ip_address = $_SERVER['REMOTE_ADDR']."\r\n";
    }

$f = fopen('../../Logs/Saved-IP/IP-Address.txt', 'a');
fwrite($f, $ip_address);
fclose($f);
