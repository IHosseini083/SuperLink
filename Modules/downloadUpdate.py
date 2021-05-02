from zipfile import ZipFile

from requests import get


class GetNewUpdate:
    def __init__(self, update_link: str = None):
        self.update_link = update_link
        if self.update_link is None:
            self.update_link = "https://github.com/IHosseini083/SuperLink/archive/refs/heads/main.zip"
        else:
            pass

    def download(self, filename):
        req = get(self.update_link)
        with open(filename, "wb") as f:
            f.write(req.content)

    def extract(self, filename, path):
        with ZipFile(filename, "r") as zip_file:
            zip_file.extractall(path=path)
