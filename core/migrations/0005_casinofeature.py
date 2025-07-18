# Generated by Django 4.2.9 on 2025-07-03 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_casino_bonus_amount_casino_bonus_percent_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CasinoFeature",
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
                ("text", models.CharField(max_length=255)),
                (
                    "casino",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="features",
                        to="core.casino",
                    ),
                ),
            ],
        ),
    ]
