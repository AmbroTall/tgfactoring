# Generated by Django 4.1.5 on 2023-02-06 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0007_loans_partner_1_address_loans_partner_1_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loans',
            name='partner_1_DOB',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loans',
            name='partner_2_DOB',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loans',
            name='partner_3_DOB',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loans',
            name='partner_4_DOB',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loans',
            name='partner_5_DOB',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
    ]
