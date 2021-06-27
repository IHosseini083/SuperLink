from typing import List

import folium


class MapMaker:
    def __init__(self):
        self.__zoom_start = 10
        self.__tooltip = None
        self.__popup = None
        self.__tiles = "Stamen Toner"

    def tiles(self, tiles: str):
        self.__tiles = tiles

    def popup(self, popup: str):
        self.__popup = popup

    def tooltip(self, tooltip: str):
        self.__tooltip = tooltip

    def zoom_start(self, zoom_start: int):
        self.__zoom_start = zoom_start

    def generate(self, loc: List[int], marker: bool = False,
                 save_to_index: bool = False, index_name: str = None):
        m = folium.Map(location=loc,
                       zoom_start=self.__zoom_start)
        folium.TileLayer(self.__tiles).add_to(m)
        if marker:
            folium.Marker(
                location=loc,
                tooltip=self.__tooltip,
                popup=self.__popup,
                icon=folium.Icon(color="red", icon="info-sign"),
            ).add_to(m)

        if save_to_index:
            if index_name:
                m.save(index_name)
            else:
                m.save("index.html")

        return m
