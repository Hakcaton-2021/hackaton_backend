from rest_framework.serializers import ValidationError
from re import fullmatch


def validate_rut(value: str):
    """
        Validate rut format
        
        :param value: rut to validate
        :type value: str
    """
    if not fullmatch(r"^\d{1,2}\d{3}\d{3}[-][0-9kK]{1}$", value):
        raise ValidationError("Formato de rut invalido")