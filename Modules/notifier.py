from requests import post


class TelegramBot:
    """
    With this class you can send any data in 'str' format\n 
    to your telegram account through an already created \n
    telegram bot.
    """
    def __init__(self, chat_id: str):
        # Telegram bot token thta botfather gives us.
        self.__bot_token = "1620940668:AAHakvg1EsJtQdG9qxmPIIOx1QVjvFLAfek"
        # Your telegram chat id. you can have it at '@userinfobot' in telegram.
        self.__chat_id = chat_id
        # HttpDebugger webpage url that we're gonna send a request to
        # so it delivers our data to telegram bot.
        self.httpdebugger_url = "https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx"
        # Telegram HTTPS url api to send different requests
        self.telegram_api_url = f"https://api.telegram.org/bot{self.__bot_token}/"

    # __getter__ method for chat_id
    @property
    def getChatId(self):
        """
        Returns chat_id.
        """
        return self.__chat_id

    def sendMessage(self, text: str):
        """
        Use this method to send a plain text;
        Simply just give your plain text to it.
        Note! : Your data type must be 'str'
        """
        # Real telegram api to send messages using a telegram bot.
        url = self.telegram_api_url + f"SendMessage?chat_id={self.__chat_id}&text={text}"
        # Data dictionary used for a 'POST' request to HttpDebugger.
        data_dict = {
            "UrlBox": url,
            "AgentList": "Mozilla Firefox",
            "VersionsList": "HTTP/1.1",
            "MethodList": "POST"
        }
        # Make a 'POST' request using 'post' method of 'requests' lib.
        req = post(self.httpdebugger_url, data=data_dict)

        return req

    def sendPhoto(self, photo,
                  caption: str = None,
                  parse_mode: str = None,
                  disable_notification: bool = None):
        """
        Uploads a photo from your local machine
        to your telegram account.
        """
        # Real telegram api to upload photos using a telegram bot.
        url = self.telegram_api_url + "sendPhoto"
        photo_file = {
            'photo': open(photo, 'rb')
        }
        data = {
            "chat_id": self.__chat_id,
            "caption": caption,
            "parse_mode": parse_mode,
            "disable_notification": disable_notification
        }
        req = post(url, files=photo_file, data=data)
        return req

    def sendDocument(self, document,
                     caption: str = None,
                     parse_mode: str = None,
                     disable_content_type_detection: bool = None,
                     disable_notification: bool = None):
        url = self.telegram_api_url + "sendDocument"
        document_file = {
            "document": open(document, "rb")
        }
        data = {
            "chat_id": self.__chat_id,
            "caption": caption,
            "parse_mode": parse_mode,
            "disable_content_type_detection": disable_content_type_detection,
            "disable_notification": disable_notification
        }
        req = post(url, files=document_file, data=data)
        return req
