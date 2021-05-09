# SuperLink (Social Engineering Tool)

## About SuperLink

SuperLink will host a fake website using PHP server & [Ngrok](https://ngrok.com)
and generates a link when target opens the generated link, it will request for some permissions then if it gets them,
you'll have :

- Access to target's webcam
- Longitude
- Latitude
- Accuracy
- Altitude - Not always available
- Direction - Only available if user is moving
- Speed - Only available if user is moving

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
but you must start the [@SuperLink_Delivery_Bot](http://t.me/SuperLink_Delivery_Bot) bot at first, so it can send you messages. you can have your chat id
from [here](https://t.me/userinfobot).

**Kali Linux / Ubuntu / Parrot OS**:

```bash
git clone https://github.com/IHosseini083/SuperLink.git
cd SuperLink
sudo ./linux_installer
default port for PHP server & ngrok tunnel is 4040, 
if you want to use a different one, then:
    - sudo python SuperLink.py -p PORT
otherwise:
    - sudo python3 SuperLink.py
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
Download PHP version 7 from <a href="https://windows.php.net/download#php-7.4">php.net</a>
</li>
<li>
Add php.exe to your pc <code>PATH</code>
</li>
<li>
default port for PHP server & ngrok tunnel is <code>4545</code>, if you want to use a different one, then
Enter <code>python SuperLink.py -p PORT</code> in cmd otherwise Enter <code>python SuperLink.py</code> in cmd
</li>
</ol>

## Screenshots

![SuperLink V1.3](https://github.com/IHosseini083/SuperLink/blob/main/ss/ss1.png "SuperLink version 1.3")
****
![SuperLink V1.3](https://github.com/IHosseini083/SuperLink/blob/main/ss/ss2.png "SuperLink version 1.3")
