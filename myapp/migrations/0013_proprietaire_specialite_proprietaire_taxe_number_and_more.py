# Generated by Django 4.2.3 on 2023-07-23 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_appartement_nom'),
    ]

    operations = [
        migrations.AddField(
            model_name='proprietaire',
            name='Specialite',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='proprietaire',
            name='Taxe_Number',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='proprietaire',
            name='licence',
            field=models.CharField(default='', max_length=30),
        ),
    ]
