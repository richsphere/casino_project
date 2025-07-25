# Generated by Django 4.2.9 on 2025-07-11 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0011_paymentmethod_tag_casino_deposit_methods_casino_tags_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="casino",
            name="deposit_methods",
        ),
        migrations.RemoveField(
            model_name="casino",
            name="tags",
        ),
        migrations.RemoveField(
            model_name="casino",
            name="withdrawal_methods",
        ),
        migrations.CreateModel(
            name="CasinoTag",
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
                (
                    "casino",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.casino"
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.tag"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CasinoPaymentMethod",
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
                (
                    "casino",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.casino"
                    ),
                ),
                (
                    "payment_method",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.paymentmethod",
                    ),
                ),
            ],
        ),
    ]
