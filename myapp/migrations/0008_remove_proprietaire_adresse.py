# Generated by Django 4.1.7 on 2023-06-28 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_rename_phone_message_expediteur_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proprietaire',
            name='adresse',
        ),
    ]
