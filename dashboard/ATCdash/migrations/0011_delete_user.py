# Generated by Django 4.2 on 2023-04-15 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ATCdash', '0010_delete_userlogentry'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
