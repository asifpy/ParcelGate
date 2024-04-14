# Generated by Django 5.0.2 on 2024-04-08 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Parcel",
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
                ("block_number", models.CharField(max_length=50)),
                ("neighbourhood", models.CharField(max_length=100)),
                ("subdivision_number", models.CharField(max_length=50)),
                (
                    "land_use_group",
                    models.CharField(
                        choices=[
                            ("Agricultural", "Agricultural"),
                            ("Residential", "Residential"),
                            ("Commercial", "Commercial"),
                        ],
                        max_length=50,
                    ),
                ),
                ("description", models.TextField()),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
