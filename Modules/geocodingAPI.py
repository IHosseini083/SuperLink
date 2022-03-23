from json import loads

from requests import get


class Geocoding:
    """
    Forward & Reverse Geocoding based on OpenStreetMap data.\n
    Find geocoordinates (`latitude` and `longitude`)\n
    for an address or use reverse geocoding to define\n
    positions for asset tracking and more.
    """

    def __init__(self) -> None:
        self._api_version = "1.0"
        self._api_key = "8283dc8844msha6f0c368763b836p1f6054jsn3278c2899b98"
        self._api_host = "forward-reverse-geocoding.p.rapidapi.com"
        self._api_base_url = "https://forward-reverse-geocoding.p.rapidapi.com/v1"
        self._headers = {
            "x-rapidapi-key": self._api_key,
            "x-rapidapi-host": self._api_host
        }

    def __repr__(self) -> str:
        return f"{__class__.__name__}(v{self._api_version})"

    def reverse(self, lat: str, lon: str,
                zoom: str = None,
                limit: str = None,
                format: str = "json") -> dict:
        """
        Find address or place by `latitude` and `longitude`\n
        """
        params = {
            "lat": lat,
            "lon": lon,
            "format": format,
            "accept-language": "en",
            "polygon_threshold": "0.0"
        }
        if zoom:
            params["zoom"] = zoom
        if limit:
            params["limit"] = limit
        url = f'{self._api_base_url}/reverse'
        req = get(url, params=params, headers=self._headers)
        return loads(req.text) if format == "json" else req.text

    def forward(self, street: str, city: str,
                state: str, postal_code: str,
                county: str = None, country: str = None,
                format: str = "json"):
        """
        Turn an address into `latitude` and `longitude` 
        (e.g. to display on a map) by schematic input.
        """
        params = {
            "format": format,
            "street": street,
            "city": city,
            "state": state,
            "postalcode": postal_code,
            "accept-language": "en",
            "polygon_threshold": "0.0"
        }
        if county:
            params["county"] = county
        if country:
            params["country"] = country
        url = f'{self._api_base_url}/forward'
        req = get(url, params=params, headers=self._headers)
        return loads(req.text) if format == "json" else req.text
