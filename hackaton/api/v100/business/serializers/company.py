from hackaton.apps.locations.services import country
from rest_framework import serializers

from hackaton.apps.business.models import (
    Company, CompanyType, Forms, Gratification,
    Country, Mutual, Bank, PaymentMobilization
)
from hackaton.apps.business.services import company as company__services

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "id",
            "business_rut",
            "business_name",
            "business_giro",
            "business_direction",
            "business_phone",
            "representative_name",
            "representative_rut",
            "representative_email",
            "billing_rut",
            "type",
            "form",
            "gratification",
            "country",
            "mutual",
            "mutual_amount",
            "parent",
            "checking_account",
            "checking_bank",
            "payment_mobilization",
            "created_at",
            "updated_at",
        ]

class CreateSerializer(serializers.ModelSerializer):
    business_rut = serializers.CharField(max_length=100, required=True, )
    business_name = serializers.CharField(max_length=300, required=False, allow_blank=True)
    business_giro = serializers.CharField(max_length=600, required=False, allow_blank=True)
    business_direction = serializers.CharField(max_length=600, required=False, allow_blank=True)
    business_phone = serializers.CharField(max_length=50, required=False, allow_blank=True)
    representative_name = serializers.CharField(max_length=300, required=False, allow_blank=True)
    representative_rut = serializers.CharField(max_length=100, required=False, allow_blank=True)
    representative_email = serializers.CharField(max_length=250, required=False, allow_blank=True)
    billing_rut = serializers.CharField(max_length=100, required=False, allow_blank=True)
    type = serializers.PrimaryKeyRelatedField(
        queryset=CompanyType.objects.all(), required=False, allow_null=True
    )
    form = serializers.PrimaryKeyRelatedField(
        queryset=Forms.objects.all(), required=False, allow_null=True
    )
    gratification = serializers.PrimaryKeyRelatedField(
        queryset=Gratification.objects.all(), required=False, allow_null=True
    )
    country = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(), required=False, allow_null=True
    )
    mutual = serializers.PrimaryKeyRelatedField(
        queryset=Mutual.objects.all(), required=False, allow_null=True
    )
    mutual_amount = serializers.FloatField(required=False, min_value=0.0)
    parent = serializers.IntegerField(required=False, min_value=0)
    checking_account = serializers.IntegerField(required=False, min_value=0)
    checking_bank  = serializers.PrimaryKeyRelatedField(
        queryset=Bank.objects.all(), required=False, allow_null=True
    )
    payment_mobilization = serializers.PrimaryKeyRelatedField(
        queryset=PaymentMobilization.objects.all(), required=False, allow_null=True
    )
    
    class Meta:
        model = Company
        fields = [
            "business_rut",
            "business_name",
            "business_giro",
            "business_direction",
            "business_phone",
            "representative_name",
            "representative_rut",
            "representative_email",
            "billing_rut",
            "type",
            "form",
            "gratification",
            "country",
            "mutual",
            "mutual_amount",
            "parent",
            "checking_account",
            "checking_bank",
            "payment_mobilization",
        ]

    def create(self, validated_data):
        company = company__services.create_compony(
            business_rut=validated_data["business_rut"],
            business_name=validated_data["business_name"] if "business_name" in validated_data else None,
            business_giro=validated_data["business_giro"] if "business_giro" in validated_data else None,
            business_direction=validated_data["business_direction"] if "business_direction" in validated_data else None,
            business_phone=validated_data["business_phone"] if "business_phone" in validated_data else None,
            representative_name=validated_data["representative_name"] if "representative_name" in validated_data else None,
            representative_rut=validated_data["representative_rut"] if "representative_rut" in validated_data else None,
            representative_email=validated_data["representative_email"] if "representative_email" in validated_data else None,
            billing_rut=validated_data["billing_rut"] if "billing_rut" in validated_data else None,
            type=validated_data["type"] if "type" in validated_data else None,
            form=validated_data["form"] if "form" in validated_data else None,
            gratification=validated_data["gratification"] if "gratification" in validated_data else None,
            country=validated_data["country"] if "country" in validated_data else None,
            mutual=validated_data["mutual"] if "mutual" in validated_data else None,
            mutual_amount=validated_data["mutual_amount"] if "mutual_amount" in validated_data else None,
            parent=validated_data["parent"] if "parent" in validated_data else None,
            checking_account=validated_data["checking_account"] if "checking_account" in validated_data else None,
            checking_bank=validated_data["checking_bank"] if "checking_bank" in validated_data else None,
            payment_mobilization=validated_data["payment_mobilization"]  if "payment_mobilization" in validated_data else None,
        )

        return company

class UpdateSerializer(serializers.ModelSerializer):
    business_rut = serializers.CharField(max_length=100, required=True, )
    business_name = serializers.CharField(max_length=300, required=False, allow_blank=True)
    business_giro = serializers.CharField(max_length=600, required=False, allow_blank=True)
    business_direction = serializers.CharField(max_length=600, required=False, allow_blank=True)
    business_phone = serializers.CharField(max_length=50, required=False, allow_blank=True)
    representative_name = serializers.CharField(max_length=300, required=False, allow_blank=True)
    representative_rut = serializers.CharField(max_length=100, required=False, allow_blank=True)
    representative_email = serializers.CharField(max_length=250, required=False, allow_blank=True)
    billing_rut = serializers.CharField(max_length=100, required=False, allow_blank=True)
    type = serializers.PrimaryKeyRelatedField(
        queryset=CompanyType.objects.all(), required=False, allow_null=True
    )
    form = serializers.PrimaryKeyRelatedField(
        queryset=Forms.objects.all(), required=False, allow_null=True
    )
    gratification = serializers.PrimaryKeyRelatedField(
        queryset=Gratification.objects.all(), required=False, allow_null=True
    )
    country = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(), required=False, allow_null=True
    )
    mutual = serializers.PrimaryKeyRelatedField(
        queryset=Mutual.objects.all(), required=False, allow_null=True
    )
    mutual_amount = serializers.FloatField(required=False, min_value=0.0)
    parent = serializers.IntegerField(required=False, min_value=0)
    checking_account = serializers.IntegerField(required=False, min_value=0)
    checking_bank  = serializers.PrimaryKeyRelatedField(
        queryset=Bank.objects.all(), required=False, allow_null=True
    )
    payment_mobilization = serializers.PrimaryKeyRelatedField(
        queryset=PaymentMobilization.objects.all(), required=False, allow_null=True
    )
   


    class Meta:
        model = Company
        fields = [
            "business_rut",
            "business_name",
            "business_giro",
            "business_direction",
            "business_phone",
            "representative_name",
            "representative_rut",
            "representative_email",
            "billing_rut",
            "type",
            "form",
            "gratification",
            "country",
            "mutual",
            "mutual_amount",
            "parent",
            "checking_account",
            "checking_bank",
            "payment_mobilization",
        ]
    
    def update(self, instance, validated_data):
        instance.business_rut = validated_data["business_rut"]
        instance.business_name = validated_data["business_name"]
        instance.business_giro = validated_data["business_giro"]
        instance.business_direction = validated_data["business_direction"]
        instance.business_phone = validated_data["business_phone"]
        instance.representative_name = validated_data["representative_name"]
        instance.representative_rut = validated_data["representative_rut"]
        instance.representative_email = validated_data["representative_email"]
        instance.billing_rut = validated_data["billing_rut"]
        instance.type = validated_data["type"]
        instance.form = validated_data["form"]
        instance.gratification = validated_data["gratification"]
        instance.country = validated_data["country"]
        instance.mutual = validated_data["mutual"]
        instance.mutual_amount = validated_data["mutual_amount"]
        instance.parent = validated_data["parent"]
        instance.checking_account = validated_data["checking_account"]
        instance.checking_bank = validated_data["checking_bank"]
        instance.payment_mobilization = validated_data["payment_mobilization"]
        instance.save(
            update_fields=[
                "business_rut",
                "business_name",
                "business_giro",
                "business_direction",
                "business_phone",
                "representative_name",
                "representative_rut",
                "representative_email",
                "billing_rut",
                "type",
                "form",
                "gratification",
                "country",
                "mutual",
                "mutual_amount",
                "parent",
                "checking_account",
                "checking_bank",
                "payment_mobilization",
                "updated_at",
            ]
        )
        return instance





