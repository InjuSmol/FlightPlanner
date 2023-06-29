import math


class Airport:
    def __init__(self, code: str, latitude_degrees: float, latitude_minutes: float,
                 longitude_degrees: float, longitude_minutes: float):
        self.code = code
        self.latitude_degrees = latitude_degrees
        self.latitude_minutes = latitude_minutes
        self.longitude_degrees = longitude_degrees
        self.longitude_minutes = longitude_minutes

    def get_code(self) -> str:
        return self.code

    def get_latitude_degrees(self) -> float:
        return self.latitude_degrees

    def get_latitude_minutes(self) -> float:
        return self.latitude_minutes

    def get_longitude_degrees(self) -> float:
        return self.longitude_degrees

    def get_longitude_minutes(self) -> float:
        return self.longitude_minutes

    @staticmethod
    def calculate_distance(a1: 'Airport', a2: 'Airport') -> float:
        PI_F = math.pi
        RADIAN_FACTOR = 180.0 / PI_F
        EARTH_RADIUS = 3963.0

        lat1 = a1.latitude_degrees + a1.latitude_minutes / 60.0
        lat1 = lat1 / RADIAN_FACTOR
        long1 = -a1.longitude_degrees + a1.longitude_minutes / 60.0
        long1 = long1 / RADIAN_FACTOR
        lat2 = a2.latitude_degrees + a2.latitude_minutes / 60.0
        lat2 = lat2 / RADIAN_FACTOR
        long2 = -a2.longitude_degrees + a2.longitude_minutes / 60.0
        long2 = long2 / RADIAN_FACTOR

        x = (
            (math.sin(lat1) * math.sin(lat2))
            + (math.cos(lat1)
               * math.cos(lat2)
               * math.cos(long2 - long1))
        )
        x2 = (math.sqrt(1.0 - (x * x)) / x)
        distance = (EARTH_RADIUS * math.atan(x2))

        return distance
