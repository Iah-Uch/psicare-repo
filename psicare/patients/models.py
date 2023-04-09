from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_currentuser.db.models import CurrentUserField
from cpf_field.models import CPFField
from users.models import Student
from django_countries.fields import CountryField

# CHOICES
from .choices import FAMILY_WAGE_CHOICES, MARITAL_CHOICES, SEX_CHOICES, UF_CHOICES 

# Field Validators
from django.core.validators import MinValueValidator

# Create your models here.
class Patient(models.Model):
    created_by = CurrentUserField(related_name="patient_created_by")
    updated_by = CurrentUserField(on_update=True, related_name="patient_updated_by")
    
    res_student = models.ForeignKey(to=Student, on_delete=models.PROTECT, verbose_name="Aluno Responsável")
    
    name = models.CharField(max_length=50, verbose_name="Nome Completo")
    cpf = CPFField('CPF', unique=True)
    email = models.EmailField(unique=True)
    contact_number = PhoneNumberField(verbose_name="Telefone")
    address = models.CharField(max_length=50, verbose_name="Endereço")
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)], verbose_name="Idade")
    
    religion = models.CharField(blank=True, max_length=50, verbose_name="Religião")
    profession = models.CharField(blank=True, max_length=50, verbose_name="Profissão")
    
    marital_status = models.CharField(max_length=1,
                           choices=MARITAL_CHOICES,
                           null=False,
                           blank=False,
                           verbose_name="Estado Civil")
    
    sex = models.CharField(max_length=1,
                           choices=SEX_CHOICES,
                           null=False,
                           blank=False,
                           verbose_name="Sexo")
    
    place_of_birth = models.CharField(max_length=2,
                           choices=UF_CHOICES,
                           null=False,
                           blank=False,
                           verbose_name="Naturalidade")
    nationality = CountryField(verbose_name="Nacionalidade")
    
    family_wage = models.CharField(max_length=1,
                           choices=FAMILY_WAGE_CHOICES,
                           null=False,
                           blank=False,
                           verbose_name="Renda Familiar")
    
    scholar_affiliation = models.CharField(blank=True, max_length=35, verbose_name="Instituição de Ensino")
    treatment_bg = models.DateTimeField(blank=True, verbose_name="Início do Tratamento")
    treatment_ed = models.DateTimeField(blank=True, verbose_name="Fim do Tratamento")
    discharged = models.BooleanField(blank=True, default=False, verbose_name="Recebeu Alta")
    uni_affiliated = models.BooleanField(blank=True, default=False, verbose_name="Filiado a UNI")
    is_employee = models.BooleanField(blank=True, default=False, verbose_name="Funcionário")
    
    def __str__(self):
        return self.name    
    
    class Meta:
        verbose_name='Paciente'
        verbose_name_plural = 'Pacientes'
