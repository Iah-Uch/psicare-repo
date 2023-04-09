# Model Imports
from django.db import models
from authtools.models import AbstractNamedUser
from cpf_field.models import CPFField

# User setters imports
from .groups import GroupSetter
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractNamedUser):
    """
        Custom Base User extending Authtools AbstractNamedUser
            - Sets a 'cpf' field and defines it as login attribute.
    """    
    AbstractNamedUser._meta.get_field('name').verbose_name = 'Nome Completo'
    
    cpf = CPFField('CPF', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'cpf']

    def __str__(self):
        return self.name
    
    def check_group(self, group_list):  
        """
        Args:
            group_list(List): A list of strings

        Returns:
            bool: Checks if a user has any of the given group name(s)
        """        
        check_list=[self.groups.filter(name=i).exists() for i in group_list]
        
        return any(check_list)
    
    class Meta:
        verbose_name='Usuário'
        verbose_name_plural = 'Usuários'



class Administrator(CustomUser): # Inherits CustomUser 
    class Meta:
        verbose_name='administrador'
        verbose_name_plural = 'administradores'
        
class Secretary(CustomUser): # Inherits CustomUser 
    class Meta:
        verbose_name='Secretária'
        verbose_name_plural = 'Secretárias'

class Teacher(CustomUser): # Inherits CustomUser 
    class Meta:
        verbose_name='Professor'
        verbose_name_plural = 'Professores'

class Student(CustomUser): # Inherits CustomUser and adds three fields
    res_teacher = models.ForeignKey(to=Teacher, on_delete=models.PROTECT, verbose_name="Professor Responsável")
    
    TERM_CHOICES = ( # Term field valid choices
        ('1', '1º'),
        ('2', '2º'),
        ('3', '3º'),
        ('4', '4º'),
        ('5', '5º'),
        ('6', '6º'),
        ('7', '7º'),
        ('8', '8º'),
        ('9', '9º'),
        ('10', '10º'),
    )
    
    registration = models.CharField(max_length=7, unique=True, verbose_name="Matrícula")
    
    term = models.CharField(max_length=2,
                           choices=TERM_CHOICES,
                           null=False,
                           blank=False,
                           verbose_name="Período")
    
    active_class = models.CharField(max_length=50, verbose_name="Disciplina")
    
    class Meta:
        verbose_name='Aluno'
        verbose_name_plural = 'Alunos'



# -- Group Setting -- 
@receiver(post_save, sender=Administrator) # Administrator Group Setter
@receiver(post_save, sender=Teacher)
@receiver(post_save, sender=Secretary)
@receiver(post_save, sender=Student)
def set_group(sender, instance, *args, **kwargs):
    GroupSetter(instance, sender._meta.verbose_name_plural.title())
