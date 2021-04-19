<?php
$receive_date = date("l, Y-m-d");
$save_date = date("Y-m-d");
$imageData = $_POST['img'];

if (!empty($_POST['img'])) {
error_log("Received IMG" .$save_date. ".png | " .$receive_date. "\r\n", 3, "../../Logs/PHP-Log/WEBCAM_LOG.log");
}

$filteredData = substr($imageData, strpos($imageData, ",")+1);
$unencodedData = base64_decode($filteredData);
$fp = fopen("../../Webcam-Images/IMG".$save_date.".png", "wb");
fwrite($fp, $unencodedData);
fclose($fp);
exit();
?>

