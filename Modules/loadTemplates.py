from json import loads


class loadTemplatePath:
    def __init__(self):
        with open("./templates.json", "r") as temps:
            self.temp_data = loads(temps.read())["templates"]

    def loadPath(self, temp_index: str):
        return self.temp_data[temp_index]["path"]

    def loadName(self, temp_index: str):
        return self.temp_data[temp_index]["name"]
