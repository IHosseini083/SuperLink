from glob import glob
from os import remove, rmdir
from shutil import rmtree
from sys import exit

from colorama import Fore

LG = Fore.LIGHTGREEN_EX  # light green
LR = Fore.LIGHTRED_EX  # light red
LY = Fore.LIGHTYELLOW_EX  # light yellow
LW = Fore.LIGHTWHITE_EX  # light white
LB = Fore.LIGHTBLACK_EX  # light black
LC = Fore.LIGHTCYAN_EX  # light cyan
LM = Fore.LIGHTMAGENTA_EX  # light magneta
Y = Fore.YELLOW  # yellow


class DeleteFilesAndDirs:
    def __init__(self) -> None:
        pass

    def deleteFile(self, file_path: str):
        try:
            remove(file_path)
        except FileNotFoundError:
            print("\n" + LG + " [" + LR + "!" + LG + "]" + LY +
                  " Error:" + LW + f" [{file_path}] " + LY + "Does not exist!")
            exit()
        except IsADirectoryError:
            print("\n" + LG + " [" + LR + "!" + LG + "]" + LY +
                  " Error:" + LW + f" [{file_path}] " + LY + "Seems to be a directory not a file!")
            exit()
        except PermissionError:
            print("\n" + LG + " [" + LR + "!" + LG + "]" + LY +
                  " Error: Requires premission to delete " + LW + f"[{file_path}]")
            exit()

    def deleteEmptyDir(self, dir_path: str):
        try:
            rmdir(dir_path)
        except OSError as e:
            print("\n" + LG + " [" + LR + "!" + LG + "]" + LY + f"{e.strerror}")

    def deleteAllFilesByType(self, file_extension: str, files_path: str):
        if files_path.endswith("/"):
            files_path = files_path.replace(files_path[-1], "")
        files = glob(f'{files_path}/*.{file_extension}')
        for f in files:
            try:
                remove(f)
            except OSError as e:
                print("\n" + LG + " [" + LR + "!" + LG + "]" + LY + f"{e.strerror}")

    def deleteDirWithFiles(self, dir_path: str):
        try:
            rmtree(dir_path)
        except OSError as e:
            print("\n" + LG + " [" + LR + "!" + LG + "]" + LY + f"{e.strerror}")
