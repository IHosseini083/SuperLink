from json import loads

from requests import get


class CheckUpdates:
    def __init__(self) -> None:
        self.metadata_file = "metadata.json"
        self.current_version = self.get_version

    @property
    def checkForUpdates(self):
        try:
            ver_url = "https://raw.githubusercontent.com/IHosseini083/SuperLink/main/metadata.json"
            req = get(ver_url).text
            req = loads(req)
            github_ver = req["metadata"]["version"]
            if github_ver != self.current_version:
                return github_ver
            else:
                return False
        except Exception as error:
            return None

    @property
    def get_version(self):
        with open(self.metadata_file, "r") as meta_file:
            content = meta_file.read()
            ver = loads(content)
            ver = ver["metadata"]["version"]
            return ver
