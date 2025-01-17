# Generated by Django 5.0.4 on 2024-04-22 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Recipe",
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
                ("recipe_name", models.CharField(max_length=100)),
                ("recipe_description", models.TextField()),
                ("recipe_image", models.ImageField(upload_to="files")),
            ],
        ),
    ]
