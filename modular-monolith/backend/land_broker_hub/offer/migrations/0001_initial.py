# Generated by Django 5.0.2 on 2024-04-16 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("broker", "0002_alter_broker_options"),
        ("parcel", "0002_alter_parcel_land_use_group"),
    ]

    operations = [
        migrations.CreateModel(
            name="Offer",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "price_per_meter",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("is_active", models.BooleanField(default=False)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("last_updated_date", models.DateTimeField(auto_now=True, null=True)),
                (
                    "broker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="broker.broker"
                    ),
                ),
                ("parcels", models.ManyToManyField(to="parcel.parcel")),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
    ]
