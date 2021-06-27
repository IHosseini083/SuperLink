echo ' [#] Updating Packages...'
apt-get update
echo ' ------------------------- '
echo ' [>] Installing Dependencies...'
echo ' [>] Installing Python3'
apt-get -y install python3 python3-pip
echo ' [>] Installing PHP'
apt-get -y install php
echo ' [>] Installing Requests'
pip3 install requests
echo ' [>] Installing Colorama'
pip3 install colorama
echo ' [>] Installing Pyngrok'
pip3 install pyngrok
echo ' [>] Installing Pillow'
pip3 install Pillow
echo ' [>] Installing Zipfile36'
pip3 install zipfile36
echo ' [>] Installing Argparse'
pip3 install argparse
echo ' [>] Setting Permissions...'
chmod 777 Templates
chmod 777 Logs
chmod 777 Target-Data
chmod 777 Webcam-Images
chmod 777 Modules
chmod 777 config.json
chmod 777 templates.json
echo ' ------------------------- '
echo ' [#] Installed !'
