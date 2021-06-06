from json import loads

from requests import get


class GeolocationIP:
    def __init__(self, ip_addr):
        self.ip_addr = ip_addr
        # Exclusive GeoIP web-api by SuperLink developer (IHosseini)
        self.api_url = f"http://webapiccg.herokuapp.com/geo/?ip={self.ip_addr}"

    @property
    def get_data(self):
        req = get(self.api_url)
        status_code = 200 if req.status_code == 200 and loads(req.text)["status"] == 200 else 404
        data = loads(req.text)["data"]
        if status_code == 200:
            city = data["city"]
            region = data["region"]
            country = data["country"]
            loc = data["location"]
            asn = data["server"]
            postal = data["postal"]
            timezone = data["time_zone"]
            data_dict = {
                "ip": self.ip_addr,
                "city": city,
                "region": region,
                "country": country,
                "location": loc,
                "asn": asn,
                "postal": postal,
                "time_zone": timezone
            }
            return data_dict
        else:
            return None
