# Generated by Django 5.1.5 on 2025-01-18 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatuser',
            options={'verbose_name': 'Chat User', 'verbose_name_plural': 'Chat Users'},
        ),
    ]
