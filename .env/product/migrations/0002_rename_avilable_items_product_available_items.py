# Generated by Django 4.0.3 on 2022-03-07 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='avilable_items',
            new_name='available_items',
        ),
    ]
