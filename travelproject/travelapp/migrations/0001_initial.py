# Generated by Django 4.1.4 on 2022-12-06 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Details",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("img", models.ImageField(upload_to="pics")),
                ("des", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Palce",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("img", models.ImageField(upload_to="pics")),
                ("desc", models.TextField()),
            ],
        ),
    ]
