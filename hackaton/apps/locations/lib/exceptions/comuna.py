class CantCreateComuna(BaseException):
    pass


class CantUpdateComuna(BaseException):
    pass


class CantUpdateComunaStatus(CantUpdateComuna):
    pass
