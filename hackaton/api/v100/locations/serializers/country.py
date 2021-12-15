from rest_framework import serializers

from hackaton.apps.locations.models import Country
from hackaton.apps.locations.services import country as country_services
from hackaton.utils.error_handler import ErrorHandler


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = [
            "pk",
            "code",
            "name",
            "is_active",
            "created_at",
            "updated_at",
        ]


class CreateSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=300)

    class Meta:
        model = Country
        fields = [
            "code",
            "name",
        ]

    def validate(self, data):
        error_handler = ErrorHandler()

        if country_services.get_country_by_name(name=data["name"]):
            error_handler.handle_error(
                field_name="name",
                error="Ya existe un pais con este nombre",
            )
        if error_handler.have_errors():
            raise error_handler.raise_errors()
        return data

    def create(self, validated_data):
        country = country_services.create_country(
            code=validated_data["code"],
            name=validated_data["name"],
        )
        return country


class UpdateSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=255)

    class Meta:
        model = Country
        fields = [
            "code",
            "name",
        ]

    def validate(self, data):
        instance = getattr(self, "instance", None)
        same_name = instance.name == data["name"]
        error_handler = ErrorHandler()

        if country_services.get_country_by_name(name=data["name"]) and not same_name:
            error_handler.handle_error(
                field_name="name",
                error="Ya existe un pais con este nombre",
            )
        if error_handler.have_errors():
            raise error_handler.raise_errors()
        return data

    def update(self, instance, validated_data):
        instance.code = validated_data["code"]
        instance.name = validated_data["name"]
        instance.save(
            update_fields=[
                "code",
                "name",
                "updated_at",
            ]
        )
        return instance
