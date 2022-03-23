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
            elif self.load_token == "":
                self.update_config_file("ngrok", {"token": self.get_token})
            elif self.load_chat_id == "":
                self.update_config_file("telegram", {"chat_id": self.get_chat_id})
            elif self.load_region == "":
                self.update_config_file("ngrok", {"region": "au"})
        else:
            self.create_configfile()

    def load_conf_file(self, index: str, p: str):
        with open(self.config_file, "r") as file:
            data = loads(file.read())[index][p]
        return data

    def update_config_file(self, index: str, new_config: dict):
        with open(self.config_file, "r") as file:
            data = loads(file.read())
            data[index].update(new_config)
        with open(self.config_file, "w") as file:
            file.write(dumps(data))

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
        if tg_chat_id != "":
            return tg_chat_id
        print(LR + "\n [!] Chat id was not received!")
        exit()

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
        with open(self.config_file, "w") as file:
            data = dumps(data_dict)
            file.write(data)

    @property
    def load_token(self):
        return self.load_conf_file("ngrok", "token")

    @property
    def load_chat_id(self):
        return self.load_conf_file("telegram", "chat_id")

    @property
    def load_region(self):
        return self.load_conf_file("ngrok", "region")
