# Generated by Django 4.2.3 on 2024-11-09 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizsession',
            name='session_code',
            field=models.CharField(max_length=100),
        ),
    ]