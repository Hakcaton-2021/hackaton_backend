# Generated by Django 3.2.9 on 2021-12-15 19:26

from django.db import migrations
from hackaton.apps.central.models import CompensationBox, Mutual

from hackaton.apps.locations.models import Country


def init(apps, schema_editor):
    country_code = "CL"
    country = Country.objects.filter(code=country_code).first()
    compensation_box = [
        {"code": "losandes", "name": "Caja Los Andes"},
        {"code": "araucana", "name": "La Araucana"},
        {"code": "losheores", "name": "Los Heores"},
        {"code": "gabriela", "name": "Gabriela Mistral"},
        {"code": "18septiembre", "name": "18 de Septiembre"},
        {"code": "sinccaf", "name": "Sin CCAF"},
    ]
    
    mutual = [
        {"code": "ACHS", "name": "ACHS"},
        {"code": "MUTUAL", "name": "Mutual"},
        {"code": "IST", "name": "IST"},
    ]

    create(CompensationBox, compensation_box, country)
    create(Mutual, mutual, country)


def create(objeto, items, country):
    for item in items:
        obj = objeto.objects.filter(code=item.get("code")).first()
        if not obj:
            obj = objeto()
            obj.code = item.get("code")
            obj.name=item.get("name")
            obj.country=country
        else:
            obj.name = item.get("name")
        obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('central', '0002_auto_20211215_1548'),
    ]

    operations = [migrations.RunPython(init)]
