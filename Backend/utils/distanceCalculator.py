def calculate_distance(a1, a2):
    PI_F = 3.1415927
    RADIAN_FACTOR = 180.0 / PI_F
    EARTH_RADIUS = 3963.0

    lat1 = a1.latitudeDegrees + a1.latitudeMinutes / 60.0
    long1 = -a1.longitudeDegrees + a1.longitudeMinutes / 60.0
    lat2 = a2.latitudeDegrees + a2.latitudeMinutes / 60.0
    long2 = -a2.longitudeDegrees + a2.longitudeMinutes / 60.0

    x = (
        (math.sin(lat1 / RADIAN_FACTOR) * math.sin(lat2 / RADIAN_FACTOR))
        + (math.cos(lat1 / RADIAN_FACTOR)
           * math.cos(lat2 / RADIAN_FACTOR)
           * math.cos((long2 / RADIAN_FACTOR) - (long1 / RADIAN_FACTOR)))
    )
    x2 = math.sqrt(1.0 - (x * x)) / x
    distance = EARTH_RADIUS * math.atan(x2)

    return distance
