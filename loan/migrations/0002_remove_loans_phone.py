# Generated by Django 4.1.5 on 2023-01-16 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loans',
            name='phone',
        ),
    ]