from json import loads


class loadTemplatePath:
    def __init__(self):
        with open("./templates.json", "r") as temps:
            self.temp_data = loads(temps.read())["templates"]

    def loadPath(self, temp_index: str):
        temp_path = self.temp_data[temp_index]["path"]
        return temp_path

    def loadName(self, temp_index: str):
        temp_name = self.temp_data[temp_index]["name"]
        return temp_name
