class CantCreateCountry(BaseException):
    pass

class CantUpdateCountry(BaseException):
    pass

class CantUpdateCountryStatus(CantUpdateCountry):
    pass
