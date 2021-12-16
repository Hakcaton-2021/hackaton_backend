from hackaton.apps.locations.services import country
from rest_framework import serializers

from hackaton.apps.business.models import (
    Company, CostCenter
    
)
from hackaton.apps.business.services import cost_center as cost_center_services

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCenter
        fields = [
            "id",
            "company",
            "name",
            "code",
            "parent",
            "created_at",
            "updated_at",
        ]

class CreateSerializer(serializers.ModelSerializer):
    company =serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), required=False, allow_null=True
    )
    name = serializers.CharField(max_length=300, required=False, allow_blank=True)
    code = serializers.CharField(max_length=100, required=False, allow_blank=True)
    parent = serializers.IntegerField(required=False, min_value=0)
    
    class Meta:
        model = CostCenter
        fields = [
            "company",
            "name",
            "code",
            "parent",
        ]

    def create(self, validated_data):
        cost_center = cost_center_services.create_cost_center(
            company=validated_data["company"],
            name=validated_data["name"],
            code=validated_data["code"],
            parent=validated_data["parent"],
        )
        return cost_center

class UpdateSerializer(serializers.ModelSerializer):
    company =serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), required=False, allow_null=True
    )
    name = serializers.CharField(max_length=300, required=False, allow_blank=True)
    code = serializers.CharField(max_length=100, required=False, allow_blank=True)
    parent = serializers.IntegerField(required=False, min_value=0)

    class Meta:
        model = CostCenter
        fields = [
            "company",
            "name",
            "code",
            "parent",
        ]
    
    def update(self, instance, validated_data):
        instance.company = validated_data["company"]
        instance.name = validated_data["name"]
        instance.code = validated_data["code"]
        instance.parent = validated_data["parent"]
        instance.save(
            update_fields=[
                "company",
                "name",
                "code",
                "parent",
                "updated_at",
            ]
        )
        return instance





