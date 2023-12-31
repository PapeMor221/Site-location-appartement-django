# Generated by Django 4.1.7 on 2023-06-28 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_proprietaire_adresse'),
    ]

    operations = [
        migrations.AddField(
            model_name='appartement',
            name='profil_photo',
            field=models.ImageField(default='', upload_to='Profil_Appartement/'),
        ),
        migrations.AddField(
            model_name='proprietaire',
            name='profil_photo',
            field=models.ImageField(default='', upload_to='Profil_Proprietaire/'),
        ),
    ]
