# Generated by Django 2.1.4 on 2018-12-12 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='number',
            new_name='id_number',
        ),
    ]
