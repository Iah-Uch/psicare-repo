# Generated by Django 3.2.16 on 2022-12-09 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20221209_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_secretary',
            field=models.BooleanField(default=False),
        ),
    ]
