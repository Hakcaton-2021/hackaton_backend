# Generated by Django 3.2.9 on 2021-12-15 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("locations", "0003_auto_20211215_0938"),
    ]

    operations = [
        migrations.AddField(
            model_name="comuna",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]