# Generated by Django 3.2.4 on 2021-07-31 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='admin',
            new_name='Article',
        ),
    ]
