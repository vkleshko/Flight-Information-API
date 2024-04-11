# Generated by Django 4.1.7 on 2024-01-15 17:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("airport_service", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="airport",
            old_name="closet_big_city",
            new_name="closest_big_city",
        ),
        migrations.AlterUniqueTogether(
            name="airport",
            unique_together={("name", "closest_big_city")},
        ),
    ]