# Generated by Django 4.1 on 2023-09-24 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FakeNews_model",
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
                ("text", models.TextField(max_length=2000)),
                ("subject", models.CharField(max_length=20)),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
