class CantCreateCost_Center(BaseException):
    pass

class CantUpdateCost_Center(BaseException):
    pass

class CantUpdateCost_CenterStatus(CantUpdateCost_Center):
    pass
