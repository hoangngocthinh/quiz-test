# Generated by Django 4.2.3 on 2023-12-23 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_user_email"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Person",
        ),
    ]
