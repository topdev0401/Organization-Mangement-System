# Generated by Django 2.1.4 on 2019-01-16 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='facility',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]