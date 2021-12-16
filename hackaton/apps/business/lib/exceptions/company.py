class CantCreateCompany(BaseException):
    pass

class CantUpdateCompany(BaseException):
    pass

class CantUpdateCompanyStatus(CantUpdateCompany):
    pass
