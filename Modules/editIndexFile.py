class EditIndexFile:
    def __init__(self, template_path, down_link=None, redir_link=None):
        self.template_path = template_path
        self.down_link = down_link
        self.redir_link = redir_link
        with open(self.template_path + "/main.html", "r") as mainFile:
            self.main_html_file = mainFile.read()

    def WriteToIndexFile(self, data):
        with open(self.template_path + "/index.html", "w") as indexFile:
            indexFile.write(data)

    def ChangeToDownFile(self):
        download_file = self.main_html_file.replace("DOWNLOAD_LINK", self.down_link)
        download_file = download_file.replace("SOME_FUNC", "downloadFile()")
        self.WriteToIndexFile(download_file)

    def ChangeToGetDataFile(self):
        getdata_file = self.main_html_file.replace("SOME_FUNC", "information()")
        self.WriteToIndexFile(getdata_file)

    def ChangeToRedirFile(self):
        redir_file = self.main_html_file.replace("REDIR_LINK", self.redir_link)
        redir_file = redir_file.replace("SOME_FUNC", "redirectUrl()")
        self.WriteToIndexFile(redir_file)
