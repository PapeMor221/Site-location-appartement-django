# Generated by Django 4.1.7 on 2023-06-28 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_message_expediteur_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='phone',
            field=models.CharField(default='', max_length=100),
        ),
    ]
