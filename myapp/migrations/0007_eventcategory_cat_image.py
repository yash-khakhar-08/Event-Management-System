# Generated by Django 5.0.1 on 2025-02-16 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_eventcategory_event_event_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventcategory',
            name='cat_image',
            field=models.ImageField(default='', upload_to='category_pics/'),
        ),
    ]
