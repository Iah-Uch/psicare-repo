from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name="Nome")
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    registration = models.IntegerField(verbose_name="Matrícula", validators=[MinValueValidator(1), MaxValueValidator(99999999)])
    term = models.IntegerField(verbose_name="Período", validators=[MinValueValidator(1)])
    active_class = models.CharField(max_length=50, verbose_name="Disciplina")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"({self.registration}) - {self.name}"