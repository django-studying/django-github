# Generated by Django 4.1.2 on 2022-11-24 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_remove_main_barlist_urls_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_barlist',
            name='urls_field',
            field=models.URLField(default='http://'),
        ),
    ]