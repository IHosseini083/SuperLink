from json import loads

from requests import get


class CheckUpdates:
    def __init__(self) -> None:
        self.metadata_file = "metadata.json"

    @property
    def new_update(self):
        try:
            ver_url = "https://raw.githubusercontent.com/IHosseini083/SuperLink/main/metadata.json"
            req = get(ver_url).text
            req = loads(req)
            github_ver = req["metadata"]["version"]
            github_changelog = req["metadata"]["changelog"]
            str_github_ver = str(github_ver).replace(".", "")
            str_current_ver = str(self.get_info[0]).replace(".", "")
            changelog = self.get_info[1]
            if github_ver != self.get_info[0]:
                if int(str_github_ver) < int(str_current_ver):
                    return False
                else:
                    return github_ver, github_changelog
            else:
                return False
        except Exception:
            return None

    @property
    def get_info(self):
        with open(self.metadata_file, "r") as meta_file:
            content = meta_file.read()
            info = loads(content)
            ver = info["metadata"]["version"]
            changelog = info["metadata"]["changelog"]
            return ver, changelog
