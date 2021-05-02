from json import dumps, loads
from os import path, stat

from colorama import Fore

LG = Fore.LIGHTGREEN_EX  # light green
LR = Fore.LIGHTRED_EX  # light red
LY = Fore.LIGHTYELLOW_EX  # light yellow
LW = Fore.LIGHTWHITE_EX  # light white
LB = Fore.LIGHTBLACK_EX  # light black
LC = Fore.LIGHTCYAN_EX  # light cyan
LM = Fore.LIGHTMAGENTA_EX  # light magneta
Y = Fore.YELLOW  # yellow


class CheckConfigFile:
    def __init__(self):
        self.config_file = "config.json"
        if path.exists(self.config_file) is True:
            if stat(self.config_file).st_size == 0:
                self.create_configfile()
            else:
                if self.loadToken == "":
                    self.updateConfigFile("ngrok", {"token": self.get_token})
                elif self.loadChatId == "":
                    self.updateConfigFile("telegram", {"chat_id": self.get_chat_id})
                elif self.loadRegion == "":
                    self.updateConfigFile("ngrok", {"region": "us"})
                else:
                    pass
        else:
            self.create_configfile()

    def loadConfFile(self, index: str, property: str):
        with open(self.config_file, "r") as cfile:
            jdata = loads(cfile.read())[index][property]
        return jdata

    def updateConfigFile(self, index: str, new_config: dict):
        with open(self.config_file, "r") as cfile:
            jdata = loads(cfile.read())
            jdata[index].update(new_config)
        with open(self.config_file, "w") as cfile:
            cfile.write(dumps(jdata))

    @property
    def get_token(self):
        token = input(Y + "\n [!] Please enter your 'ngrok authentication token' : " + LW + "")
        if token == "":
            print(LR + "\n [!] Token was not received!")
            exit()
        elif len(token) < 49:
            print(LR + "\n [!] Entered token does not seem valid")
            exit()
        else:
            return token

    @property
    def get_chat_id(self):
        tg_chat_id = input(Y + "\n [!] Please enter your 'telegram chat id' (find it here @userinfobot) : " + LW + "")
        if tg_chat_id == "":
            print(LR + "\n [!] Chat id was not received!")
            exit()
        else:
            return tg_chat_id

    def create_configfile(self):
        data_dict = {
            "ngrok": {
                "token": self.get_token,
                "region": "us"
            },
            "telegram": {
                "chat_id": self.get_chat_id
            }
        }
        with open(self.config_file, "w") as cfile:
            jdata = dumps(data_dict)
            cfile.write(jdata)

    @property
    def loadToken(self):
        token = self.loadConfFile("ngrok", "token")
        return token

    @property
    def loadRegion(self):
        region = self.loadConfFile("ngrok", "region")
        return region

    @property
    def loadChatId(self):
        chat_id = self.loadConfFile("telegram", "chat_id")
        return chat_id

    @property
    def loadRegion(self):
        region = self.loadConfFile("ngrok", "region")
        return region
