# Generated by Django 4.2.3 on 2024-04-24 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_country_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.CharField(blank=True, max_length=1200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='avatar_thumb',
            field=models.CharField(blank=True, max_length=1200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='user',
            name='enabled_2fa',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
