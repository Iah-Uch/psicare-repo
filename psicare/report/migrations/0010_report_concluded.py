# Generated by Django 3.2.16 on 2022-11-29 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0009_auto_20221125_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='concluded',
            field=models.BooleanField(blank=True, default=False, verbose_name='Concluído'),
        ),
    ]