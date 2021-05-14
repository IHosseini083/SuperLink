<?php
header('Content-Type: text/html');
{
  $latitude = $_POST['latitude'];
  $longitude = $_POST['longitude'];
  $accuracy = $_POST['accuracy'];
  $altitude = $_POST['altitude'];
  $direction = $_POST['direction'];
  $speed = $_POST['speed'];

  $data['loc_info'] = array(
    'latitude' => $latitude,
    'longitude' => $longitude,
    'accuracy' => $accuracy,
    'altitude' => $altitude,
    'direction' => $direction,
    'speed' => $speed,
  );
  $jdata = json_encode($data);

  $f = fopen('../../Logs/Saved-Info/Loc-Info.json', 'w');
  fwrite($f, $jdata);
  fclose($f);
}
?>
