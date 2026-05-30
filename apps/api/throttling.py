from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class BurstRateThrottle(UserRateThrottle):
    rate = "60/min"


class SustainedRateThrottle(UserRateThrottle):
    rate = "1000/day"


class PublicAnonThrottle(AnonRateThrottle):
    rate = "20/min"


class LoginRateThrottle(AnonRateThrottle):
    rate = "5/min"

