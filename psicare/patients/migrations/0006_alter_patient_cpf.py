# Generated by Django 3.2.16 on 2022-12-01 19:19

import cpf_field.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_auto_20221201_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='cpf',
            field=cpf_field.models.CPFField(max_length=14, verbose_name='CPF'),
        ),
    ]