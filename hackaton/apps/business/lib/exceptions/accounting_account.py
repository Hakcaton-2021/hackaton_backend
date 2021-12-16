class CantCreateAccountingAccount(BaseException):
    pass

class CantUpdateAccountingAccount(BaseException):
    pass

class CantUpdateAccountingAccountStatus(CantUpdateAccountingAccount):
    pass
