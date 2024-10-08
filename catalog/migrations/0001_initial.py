# Generated by Django 5.1 on 2024-08-27 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=64, verbose_name="name")),
                (
                    "description",
                    models.CharField(max_length=64, verbose_name="description"),
                ),
            ],
            options={
                "verbose_name": "Categy",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=64, verbose_name="name")),
                (
                    "description",
                    models.CharField(max_length=64, verbose_name="description"),
                ),
                (
                    "image",
                    models.ImageField(upload_to="media/catalog", verbose_name="image"),
                ),
                ("price", models.IntegerField(verbose_name="price")),
                (
                    "created_at",
                    models.DateField(auto_now_add=True, verbose_name="created"),
                ),
                ("update_at", models.DateField(auto_now=True, verbose_name="created")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.category",
                        verbose_name="category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
    ]
