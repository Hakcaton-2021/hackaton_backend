# Generated by Django 3.2.9 on 2021-12-17 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_auto_20211217_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='mutual_amount',
            field=models.FloatField(default=None, null=True),
        ),
    ]