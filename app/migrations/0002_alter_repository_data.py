# Generated by Django 4.0.2 on 2022-03-03 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='data',
            field=models.JSONField(blank=True),
        ),
    ]