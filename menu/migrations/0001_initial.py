# Generated by Django 4.1.7 on 2023-03-06 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MenuItem",
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
                ("name", models.CharField(max_length=150, verbose_name="Название")),
                (
                    "parents",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="head",
                        to="menu.menuitem",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пункт меню",
                "verbose_name_plural": "Пункты меню",
                "ordering": ("name",),
            },
        ),
    ]
