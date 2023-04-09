from django.db import models
from ckeditor.fields import RichTextField
from patients.models import Patient
from django_currentuser.db.models import CurrentUserField
from django.utils.html import format_html

# Create your models here.

class Report(models.Model):
    patient = models.ForeignKey(Patient, 
                             on_delete=models.PROTECT, 
                             verbose_name="Paciente")
    
    res_student = CurrentUserField()
    
    title = models.CharField(null=True, max_length=100, verbose_name="Título")
    report = RichTextField(null=True, verbose_name="Relatório")
    diagnosis = RichTextField(null=True, blank=True, verbose_name="Diagnóstico")
    file = models.FileField(null=True, blank=True, upload_to="file/", verbose_name="Arquivo")
    finished = models.BooleanField(blank=True, default=False, verbose_name="Concluído")
    
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    @property
    def html_report(self,):
        return format_html(self.report)
    
    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'