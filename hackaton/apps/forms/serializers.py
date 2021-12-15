from rest_framework import serializers


class FormSerializers(serializers.Serializer):
    name = serializers.CharField(required=True, min_length=3)
    email = serializers.EmailField(required=True, max_length=255)
    business_name = serializers.CharField(required=True, min_length=3)