import math

class Airport:
    def __init__(self, code: str, latitudeDegrees: float, latitudeMinutes: float,
                 longitudeDegrees: float, longitudeMinutes: float):
        self.code = code
        self.latitudeDegrees = latitudeDegrees
        self.latitudeMinutes = latitudeMinutes
        self.longitudeDegrees = longitudeDegrees
        self.longitudeMinutes = longitudeMinutes

    def getCode(self) -> str:
        return self.code

    def getLatitudeDegrees(self) -> float:
        return self.latitudeDegrees

    def getLatitudeMinutes(self) -> float:
        return self.latitudeMinutes

    def getLongitudeDegrees(self) -> float:
        return self.longitudeDegrees

    def getLongitudeMinutes(self) -> float:
        return self.longitudeMinutes

    @staticmethod
    def calculateDistance(a1: 'Airport', a2: 'Airport') -> float:
        PI_F = math.pi
        RADIAN_FACTOR = 180.0 / PI_F
        EARTH_RADIUS = 3963.0

        lat1 = a1.latitudeDegrees + a1.latitudeMinutes / 60.0
        lat1 = lat1 / RADIAN_FACTOR
        long1 = -a1.longitudeDegrees + a1.longitudeMinutes / 60.0
        long1 = long1 / RADIAN_FACTOR
        lat2 = a2.latitudeDegrees + a2.latitudeMinutes / 60.0
        lat2 = lat2 / RADIAN_FACTOR
        long2 = -a2.longitudeDegrees + a2.longitudeMinutes / 60.0
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
