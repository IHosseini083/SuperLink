from requests import get


class ReverseGeocoding:
    """
    Retrieve human-readable address of a  from
    `latitude` & `longitude`
    """
    def __init__(self) -> None:
        self._version = "1.0"

    def __repr__(self) -> str:
        return f"{__class__.__name__} API ({self._version})"

    @staticmethod
    def reverse(lat: str, lon: str) -> dict:
        params = {
            "lat": lat,
            "lon": lon,
            "format": "json",
            "accept-language": "en",
            "polygon_threshold": "0.0"
        }
        headers = {
            "x-rapidapi-key": "8283dc8844msha6f0c368763b836p1f6054jsn3278c2899b98",
            "x-rapidapi-host": "forward-reverse-geocoding.p.rapidapi.com"
        }
        url = "https://forward-reverse-geocoding.p.rapidapi.com/v1/reverse"
        req = get(url, params=params, headers=headers)
        return req.json()
