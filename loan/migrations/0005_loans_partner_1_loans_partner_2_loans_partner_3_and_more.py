# Generated by Django 4.1.5 on 2023-02-03 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0004_loans_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='loans',
            name='partner_1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loans',
            name='partner_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loans',
            name='partner_3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loans',
            name='partner_4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loans',
            name='partner_5',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]