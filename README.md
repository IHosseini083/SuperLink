# SuperLink (Social Engineering Tool)

![SuperLink Version](https://img.shields.io/badge/SuperLink-v1.4.5-red "SuperLink Version")
![GitHub SuperLink Size](https://img.shields.io/github/repo-size/IHosseini083/SuperLink?logoColor=red "SuperLink Size")
![GitHub License](https://img.shields.io/github/license/IHosseini083/SuperLink "License")
![Python Version](https://img.shields.io/badge/Python-3.8%2B-yellow "Python Version")
![PHP Version](https://img.shields.io/badge/PHP-7%2B-purple "PHP Version")
![Platform](https://img.shields.io/badge/Platform-Windows%2010%20|%20Linux-orange "Platform")

## NOTICE!

This repository has been archived due to low quality of its python code!

When I built this python script, It was just about a year since I started programming in python and I was not quite familiar with pythonic way of doing things or
best practice solutions for different situations and clearly I have delivered a low quality code to the community that now even I get dizzy when I look at my masterpiece :)

## Changelogs

- v1.4.4: minor bugs and issues fixed
- v1.4.5: add map maker for target's location

## About SuperLink

SuperLink will host a fake website using PHP server & [Ngrok](https://ngrok.com)
and generates a link when target opens the generated link, it will request for some permissions then if it gets them,
you'll have:

- Access to target's webcam
- Longitude
- Latitude
- Accuracy
- Altitude - Not always available
- Direction - Only available if user is moving
- Speed - Only available if user is moving
- Reverse geocoding for target's longitude, latitude

Along with Location Information it also gets Device Information without any permissions :

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
- Redirect to YouTube (for password grabber)
- Smiling moon
- Weather forecast (for location data)

## Tested on

- Kali linux (2021)
- Pop! OS (20.04)
- Windows 10

## Installation & Usage

Note!: First, go to [ngrok website](https://ngrok.com) and signup, then login and go
to [here](https://dashboard.ngrok.com/get-started/your-authtoken)
and copy your ngrok authentication token. In the first time that you run the script it will prompt you for your ngrok
authentication token, and your telegram chat id, so the script can send the generated links to your telegram account,
but you must start the [@SuperLink_Delivery_Bot](http://t.me/SuperLink_Delivery_Bot) bot at first, so it can send you
messages. you can have your chat id from [here](https://t.me/userinfobot).

**Kali Linux / Ubuntu / Parrot OS**:

```bash
git clone https://github.com/IHosseini083/SuperLink.git
cd SuperLink
sudo ./linux_installer
```

default port for **PHP** server & **ngrok** tunnel is `9090`,
if you want to use a different one, then:

```bash
sudo python3 SuperLink.py -p PORT
```

otherwise:

```bash
sudo python3 SuperLink.py
```

**Windows**:

<ol>
<li>
Download this <a href="https://github.com/IHosseini083/SuperLink/archive/refs/heads/main.zip">repository</a>
</li>
<li>
Download & install python3.8+ from <a href="https://www.python.org/">python.org</a>
</li>
<li>
Extract the <code>SuperLink-main.zip</code> zip file
</li>
<li>
Open a cmd in the extracted folder
</li>
<li>
Enter <code>pip install -r requirements.txt</code> in cmd
</li>
<li>
Download PHP version 7+ from <a href="https://windows.php.net/download">php.net</a>
</li>
<li>
Add php.exe to your pc <code>PATH</code>
</li>
<li>
default port for PHP server & ngrok tunnel is <code>9090</code>, if you want to use a different one, then
Enter <code>python SuperLink.py -p PORT</code> in cmd otherwise Enter <code>python SuperLink.py</code> in cmd
</li>
</ol>

## Screenshots

![SuperLink v1.4.5](https://github.com/IHosseini083/SuperLink/blob/main/ss/ss1.png "SuperLink v1.4.5")

---

![SuperLink v1.4.5](https://github.com/IHosseini083/SuperLink/blob/main/ss/ss2.png "SuperLink v1.4.5")
