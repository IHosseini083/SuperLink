from requests import get


class GeolocationIP:
    def __init__(self, ip_addr):
        self.ip_addr = ip_addr
        # api key from 'https://ipinfo.io/account'
        self.api_key = "32bf0de5831372"
        self.api_url = f"https://ipinfo.io/{self.ip_addr}?token={self.api_key}"

    @property
    def getData(self):
        data = get(self.api_url).json()
        try:
            city = data["city"]
            if city == "" or city is None:
                city = "n/a"
            else:
                pass
        except:
            city = "n/a"
        try:
            region = data["region"]
            if region == "" or region is None:
                region = "n/a"
            else:
                pass
        except:
            region = "n/a"
        try:
            country = data["country"]
            if country == "" or country is None:
                country = "n/a"
            else:
                pass
        except:
            country = "n/a"
        try:
            loc = data["loc"]
            if loc == "" or loc is None:
                loc = "n/a"
            else:
                pass
        except:
            loc = "n/a"
        try:
            isp = data["org"]
            if isp == "" or isp is None:
                isp = "n/a"
            else:
                pass
        except:
            isp = "n/a"
        try:
            postal = data["postal"]
            if postal == "" or postal is None:
                postal = "n/a"
            else:
                pass
        except:
            postal = "n/a"
        try:
            timezone = data["timezone"]
            if timezone == "" or timezone is None:
                timezone = "n/a"
            else:
                pass
        except:
            timezone = "n/a"

        data_dict = {
            "ip": self.ip_addr,
            "city": city,
            "region": region,
            "country": country,
            "location": loc,
            "isp": isp,
            "postal": postal,
            "time_zone": timezone
        }

        return data_dict
