# Generated by Django 5.0.1 on 2025-02-18 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_eventrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventrequest',
            name='location',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='eventrequest',
            name='state',
            field=models.CharField(default='', max_length=50),
        ),
    ]
