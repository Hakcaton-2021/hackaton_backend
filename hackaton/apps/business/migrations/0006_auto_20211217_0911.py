# Generated by Django 3.2.9 on 2021-12-17 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_auto_20211215_1546'),
        ('central', '0004_auto_20211216_0104'),
        ('business', '0005_alter_company_mutual_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='compensation_box',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='central.compensationbox'),
        ),
        migrations.AddField(
            model_name='company',
            name='comuna',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='locations.comuna'),
        ),
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='locations.country'),
        ),
    ]