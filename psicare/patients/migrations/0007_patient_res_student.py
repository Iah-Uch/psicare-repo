# Generated by Django 3.2.16 on 2022-12-07 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_student_registration'),
        ('patients', '0006_alter_patient_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='res_student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='users.student', verbose_name='Aluno Responsável'),
            preserve_default=False,
        ),
    ]