# Generated by Django 5.0.6 on 2025-04-26 17:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bookiverse", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="users",
            old_name="user_name",
            new_name="username",
        ),
    ]
