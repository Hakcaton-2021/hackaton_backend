from rest_framework import serializers

from hackaton.apps.locations.models import Comuna
from hackaton.apps.locations.services import comuna as comuna_services
from hackaton.apps.locations.services import country as country_services
from hackaton.utils.error_handler import ErrorHandler


class ListSerializer(serializers.ModelSerializer):
    country_name = serializers.ReadOnlyField(source="country.name")

    class Meta:
        model = Comuna
        fields = [
            "pk",
            "code",
            "name",
            "country_name",
            "is_active",
            "created_at",
            "updated_at",
        ]


class CreateSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=300)
    country = serializers.PrimaryKeyRelatedField(
        queryset=country_services.get_all_countries()
    )

    class Meta:
        model = Comuna
        fields = [
            "code",
            "name",
            "country",
        ]

    def validate(self, data):
        error_handler = ErrorHandler()
        if comuna_services.get_comuna_by_country(
            name=data["name"],
            country_pk=data["country"].pk,
        ):
            error_handler.handle_error(
                field_name="country",
                error="Ya existe esta comuna para el pais indicado",
            )

        if error_handler.have_errors():
            raise error_handler.raise_errors()
        return data

    def create(self, validated_data):
        comuna = comuna_services.create_country(
            code=validated_data["code"],
            name=validated_data["name"],
            country=validated_data["country"],
        )
        return comuna


class UpdateSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=300)
    country = serializers.PrimaryKeyRelatedField(
        queryset=country_services.get_all_countries()
    )

    class Meta:
        model = Comuna
        fields = [
            "code",
            "name",
            "country",
        ]

    def validate(self, data):
        instance = getattr(self, "instance", None)
        same_name = instance.name == data["name"]
        error_handler = ErrorHandler()

        if (
            comuna_services.get_comuna_by_country(
                name=data["name"], country_pk=data["country"].pk
            )
            and not same_name
        ):
            error_handler.handle_error(
                field_name="country",
                error="Ya existe esta comuna para el pais indicado",
            )
        if error_handler.have_errors():
            raise error_handler.raise_errors()
        return data

    def update(self, instance, validated_data):
        instance.code = validated_data["code"]
        instance.name = validated_data["name"]
        instance.country = validated_data["country"]
        instance.save(
            update_fields=[
                "code",
                "name",
                "country",
                "updated_at",
            ]
        )
        return instance
