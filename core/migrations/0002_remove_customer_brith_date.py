# Generated by Django 4.2 on 2023-06-26 21:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="brith_date",
        ),
    ]