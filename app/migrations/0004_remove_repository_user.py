# Generated by Django 4.0.2 on 2022-03-04 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_repository_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repository',
            name='user',
        ),
    ]
