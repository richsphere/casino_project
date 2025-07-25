# Generated by Django 4.2.9 on 2025-07-11 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_casinofeature"),
    ]

    operations = [
        migrations.CreateModel(
            name="CasinoReview",
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
                ("title", models.CharField(default="Review", max_length=255)),
                ("slug", models.SlugField(unique=True)),
                ("content_markdown", models.TextField(blank=True)),
                ("content_blocks", models.JSONField(blank=True, default=list)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "casino",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="review",
                        to="core.casino",
                    ),
                ),
            ],
            options={
                "verbose_name": "Casino Review",
                "verbose_name_plural": "Casinos Review",
            },
        ),
    ]
