# Generated by Django 3.2.9 on 2021-12-15 19:34

from django.db import migrations

from hackaton.apps.central.models import Bank
from hackaton.apps.locations.models import Country

def init(apps, schema_editor):
    country_code = "CL"
    country = Country.objects.filter(code=country_code).first()
    banks = [
        {"code": "ABN", "name": "ABN AMRO Bank"},
        {"code": "CONSO", "name": "BANCO CONSORCIO"},
        {"code": "CHILE", "name": "BANCO DE CHILE"},
        {"code": "FALAB", "name": "BANCO FALABELLA"},
        {"code": "INTER", "name": "BANCO INTERNACIONAL"},
        {"code": "RIPLE", "name": "BANCO RIPLEY"},
        {"code": "ESTADO", "name": "BANCO ESTADO"},
        {"code": "BBVA", "name": "BBVA"},
        {"code": "BCI", "name": "Banco Credito e Inversiones"},
        {"code": "BICE", "name": "BICE"},
        {"code": "COOPE", "name": "COOPEUCH"},
        {"code": "CORPB", "name": "CORPBANCA"},
        {"code": "DEUTS", "name": "DEUTSCHE BANK"},
        {"code": "HSBC", "name": "HSBC"},
        {"code": "ITAU", "name": "ITAÚ"},
        {"code": "JP MORGAN", "name": "JP MORGAN"},
        {"code": "SANTAN", "name": "SANTANDER"},
        {"code": "SCOTI", "name": "SCOTIABANK"},
        {"code": "SECURI", "name": "SECURITY"},
        ]
    for bank in banks:
        if country:
            obj = Bank.objects.filter(
                code=bank.get("code"),
                country=country).first()
            if not obj:
                obj = Bank(code=bank.get("code"), name=bank.get("name"),
                        country=country)
            else:
                obj.name = bank.get("name")
            obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(init)
    ]