# SuperLink (Social Engineering Tool)

![SuperLink_V1.0](https://github.com/IHosseini083/SuperLink/blob/main/ss/ss1.png "SuperLink version 1.0")

![Code Size](https://img.shields.io/github/languages/code-size/IHosseini083/SuperLink)![GitHub stars](https://img.shields.io/github/stars/IHosseini083/SuperLink)

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

## Installation & Usage

_Kali Linux / Ubuntu / Parrot OS_:

```
git clone https://github.com/IHosseini083/SuperLink.git
cd SuperLink
sudo ./linux_installer.sh
python3 SuperLink.py
```

_Windows_:

- Download [this repository](https://github.com/IHosseini083/SuperLink/archive/refs/heads/main.zip)
- Extract the 'SuperLink-main.zip' zip file
- Open a cmd in the extracted folder
- Enter 'pip install -r requirements.txt' on cmd
- Download PHP version 7 from [here](https://windows.php.net/download#php-7.4)
- Add php.exe to your PC PATH
- Enter 'python SuperLink.py' on cmd
