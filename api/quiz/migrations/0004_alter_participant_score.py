# Generated by Django 4.2.3 on 2024-11-09 13:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_quizsession_is_active_quizsession_max_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
