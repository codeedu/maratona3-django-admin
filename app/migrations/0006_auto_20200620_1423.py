# Generated by Django 3.0.6 on 2020-06-20 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200620_1415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='tag',
            new_name='tags',
        ),
    ]
