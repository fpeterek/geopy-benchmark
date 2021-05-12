import random
from typing import Tuple

import geopy.distance

from boundaries import Boundaries


class Point:
    def __init__(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon

    @staticmethod
    def random():
        lat = random.randint(Boundaries.down_int, Boundaries.up_int) / Boundaries.int_conv_factor
        lon = random.randint(Boundaries.left_int, Boundaries.right_int) / Boundaries.int_conv_factor
        return Point(lat=lat, lon=lon)

    @property
    def latlon(self) -> Tuple[float, float]:
        return self.lat, self.lon

    def __eq__(self, other) -> bool:
        return self.lat == other.lat and self.lon == other.lon

    def dist(self, other) -> float:
        return geopy.distance.distance(self.latlon, other.latlon).m

    def euc(self, other) -> float:
        lat2 = (self.lat - other.lat) ** 2
        lon2 = (self.lon - other.lon) ** 2
        return (lat2 + lon2) ** 0.5

    def man(self, other) -> float:
        lat = abs(self.lat - other.lat)
        lon = abs(self.lon - other.lon)
        return lat + lon

