# Model Imports
from django.db import models
from authtools.models import AbstractNamedUser

# Field Validators
from django.core.validators import MinValueValidator, MaxValueValidator

# User setters imports
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractNamedUser):
    """
        Custom Base User extending Authtools AbstractNamedUser
            - Sets a 'cpf' field and defines it as login attribute.
    """    
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['name', 'email']

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Usuário'
        verbose_name_plural = 'Usuários'


class Secretary(CustomUser): # Inherits CustomUser 
    class Meta:
        verbose_name='Secretária'
        verbose_name_plural = 'Secretárias'


class Teacher(CustomUser): # Inherits CustomUser 
    class Meta:
        verbose_name='Professor'
        verbose_name_plural = 'Professores'


class Student(CustomUser): # Inherits CustomUser and adds three fields
    registration = models.CharField(max_length=15, unique=True, verbose_name="Matrícula")
    term = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name="Período")
    active_class = models.CharField(max_length=50, verbose_name="Disciplina")
    
    class Meta:
        verbose_name='Aluno'
        verbose_name_plural = 'Alunos'



# -- Group Setters -- 
@receiver(post_save, sender=Teacher) # Teacher Group Setter
def create_teacher(sender, instance, created, **kwargs):
    if created:
        try:
            instance.groups.add(Group.objects.get(name='Professores'))
        except:
            pass

@receiver(post_save, sender=Secretary) # Secretary Group Setter
def create_secretary(sender, instance, created, **kwargs):
    if created:
        try:
            instance.groups.add(Group.objects.get(name='Secretarias'))
        except:
            pass
       
@receiver(post_save, sender=Student) # Student Group Setter
def create_student(sender, instance, created, **kwargs):
    if created:
        try:
            instance.groups.add(Group.objects.get(name='Alunos'))
        except:
            pass