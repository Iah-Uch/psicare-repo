from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_currentuser.db.models import CurrentUserField

# Field Validators
from django.core.validators import MaxValueValidator

# Create your models here.
class Patient(models.Model):
    SEX_CHOICES = ( # Sex field valid choices
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )
    
    MARITAL_CHOICES = ( # Marital Status field valid choices
        ('1', 'Solteiro'),
        ('2', 'Casado'),
        ('3', 'Separado'),
        ('4', 'Divorciado'),
        ('5', 'Viúvo')
    )
    
    created_by = CurrentUserField(related_name="patient_created_by")
    updated_by = CurrentUserField(on_update=True, related_name="patient_updated_by")
    
    name = models.CharField(max_length=50, verbose_name="Nome")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    email = models.EmailField(unique=True, blank=True)
    contact = PhoneNumberField(blank=True, verbose_name="Contato")
    address = models.CharField(blank=True, max_length=50, verbose_name="Endereço")
    age = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)], verbose_name="Idade")
    
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
    
    place_of_birth = models.CharField(blank=True, max_length=25, verbose_name="Naturalidade")
    nationality = models.CharField(blank=True, max_length=25, verbose_name="Nacionalidade")
    family_wage = models.DecimalField(blank=True, max_digits=7, decimal_places=2, verbose_name="Renda Familiar")
    scholar_affiliation = models.CharField(blank=True, max_length=35, verbose_name="Instituição de Ensino")
    treatment_bg = models.DateTimeField(null=True, blank=True, verbose_name="Início do Tratamento")
    treatment_ed = models.DateTimeField(null=True, blank=True, verbose_name="Fim do Tratamento")
    discharged = models.BooleanField(blank=True, default=False, verbose_name="Recebeu Alta")
    uni_affiliated = models.BooleanField(blank=True, default=False, verbose_name="Filiado a UNI")
    is_employee = models.BooleanField(blank=True, default=False, verbose_name="Funcionário")
    
    def __str__(self):
        return self.name    
    
    class Meta:
        verbose_name='Paciente'
        verbose_name_plural = 'Pacientes'
