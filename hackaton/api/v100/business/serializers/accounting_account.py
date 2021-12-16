from rest_framework import serializers

from hackaton.apps.business.models import (
    Company, AccountingAccount
    
)
from hackaton.apps.business.services import accounting_account as accounting_account_services

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountingAccount
        fields = [
            "id",
            "company",
            "name",
            "code",
            "created_at",
            "updated_at",
        ]

class CreateSerializer(serializers.ModelSerializer):
    company =serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), required=False, allow_null=True
    )
    name = serializers.CharField(max_length=300, required=False, allow_blank=True)
    code = serializers.CharField(max_length=100, required=False, allow_blank=True)
    
    class Meta:
        model = AccountingAccount
        fields = [
            "company",
            "name",
            "code",
        ]

    def create(self, validated_data):
        accounting_account = accounting_account_services.create_accounting_account(
            company=validated_data["company"],
            name=validated_data["name"],
            code=validated_data["code"],
        )
        return accounting_account

class UpdateSerializer(serializers.ModelSerializer):
    company =serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), required=False, allow_null=True
    )
    name = serializers.CharField(max_length=300, required=False, allow_blank=True)
    code = serializers.CharField(max_length=100, required=False, allow_blank=True)

    class Meta:
        model = AccountingAccount
        fields = [
            "company",
            "name",
            "code",
        ]
    
    def update(self, instance, validated_data):
        instance.company = validated_data["company"]
        instance.name = validated_data["name"]
        instance.code = validated_data["code"]
        instance.save(
            update_fields=[
                "company",
                "name",
                "code",
                "updated_at",
            ]
        )
        return instance





