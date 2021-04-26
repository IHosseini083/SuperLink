# SuperLink (Social Engineering Tool)

## About SuperLink

SuperLink will host a fake website using PHP server & [Ngrok](https://ngrok.com)
and generates a link when target opens the generated link, it will
request for some premissions then if it gets them, you'll have :

- Access to target's webcam
- Longitude
- Latitude
- Accuracy
- Altitude - Not always available
- Direction - Only available if user is moving
- Speed - Only available if user is moving

Along with Location Information it also get's Device Information without any permissions :

- Device Model - Not always available
- Operating System
- Platform
- Number of CPU Cores - Approximate Results
- Screen Resolution
- GPU information
- Browser Name and Version
- Public IP Address

Do other stuffs without permissions:

- Redirect target to another URL (a bad one)
- OS Password grabber (only Windows10)

## Templates

- Online camera (for webcam access)
- Mini Music player
- Redirect to youtube (for password grabber)
- Smiling moon
- Weather forcast (for location data)

## Tested on

- Kali linux (2021)
- Pop! OS (20.04)
- Windows 10

## Installation & Usage

Note!: First of all, go to [ngrok website](https://ngrok.com) and signup,
then login and go to [here](https://dashboard.ngrok.com/get-started/your-authtoken)
and copy your ngrok authentication token.
In the first time that you run the script it will prompt you
for your ngrok authentication token and your telegram chat id so
the script can send the generated links to your telegram account
but you must start the '@BadLinkM_Bot' bot at first so it can
send you messages.
you can have your chat id from [here](https://t.me/userinfobot)

*_Kali Linux / Ubuntu / Parrot OS_*:

```bash
git clone https://github.com/IHosseini083/SuperLink.git
cd SuperLink
sudo ./linux_installer.sh
-----------
Note!: default port for PHP server & ngrok tunnel is 4545, 
if you want to use a different one, then:
    - sudo python SuperLink.py -p [PORT]
otherwise:
    - sudo python3 SuperLink.py
```

*_Windows_*:

* Download [this repository](https://github.com/IHosseini083/SuperLink/archive/refs/heads/main.zip)
* Download & install python3.8+ from [python.org](https://www.python.org/)
* Extract the 'SuperLink-main.zip' zip file
* Open a cmd in the extracted folder
* Enter `pip install -r requirements.txt` in cmd
* Download PHP version 7 from [php.net](https://windows.php.net/download#php-7.4)
* Add php.exe to your PC PATH
- Note!: default port for PHP server & ngrok tunnel is `4545`, 
if you want to use a different one, then
Enter `python SuperLink.py -p [PORT]` in cmd
otherwise
Enter `python SuperLink.py` in cmd
## Screenshots

![SuperLink_V1.0](https://github.com/IHosseini083/SuperLink/blob/main/ss/ss1.png "SuperLink version 1.1")

![SuperLink_V1.0](https://github.com/IHosseini083/SuperLink/blob/main/ss/ss2.png "SuperLink version 1.1")
