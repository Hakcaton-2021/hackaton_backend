from rest_framework import serializers
from hackaton.utils.validators import validate_rut


class UnionsSerializers(serializers.Serializer):
    rut = serializers.CharField(required=True, validators=[validate_rut])
    name = serializers.CharField(required=True, min_length=3)
    code = serializers.CharField(required=False, allow_blank=True)
    active = serializers.BooleanField(required=False)
    exempt_amount = serializers.FloatField(required=False)
    exempt_amount_currency = serializers.CharField(required=False)

class FormUnionsSerializers(serializers.Serializer):
    form_id = serializers.IntegerField()
    unions = UnionsSerializers(many=True)
    
    