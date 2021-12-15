# Generated by Django 3.2.9 on 2021-12-15 18:45

from django.db import migrations

from hackaton.apps.locations.models import Country

def init(apps, schema_editor):
    countries = [
        {"code": "CL", "name": "Chile"},
        {"code": "PE", "name": "Perú"},
    ]
    for country in countries:
        obj = Country.objects.filter(code=country.get("code")).first()
        if not obj:
            obj = Country(code=country.get("code"), name=country.get("name"))
        else:
            obj.name = country.get("name")
        obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [migrations.RunPython(init)]