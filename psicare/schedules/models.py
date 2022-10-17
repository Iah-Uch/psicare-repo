from django.db import models
from django_currentuser.db.models import CurrentUserField

from patients.models import Patient
from users.models import Student

# Create your models here.
class Schedule(models.Model):
    created_by = CurrentUserField(related_name="schedule_created_by")
    updated_by = CurrentUserField(on_update=True, related_name="schedule_updated_by")
    
    patient = models.ForeignKey(Patient, 
                             on_delete=models.PROTECT, 
                             verbose_name="Paciente")
    
    student = models.ForeignKey(Student, 
                             on_delete=models.PROTECT, 
                             verbose_name="Aluno")
    
    meeting_date = models.DateTimeField(null=True, blank=True, verbose_name="Agendamento")
    
    finished = models.BooleanField(blank=True, default=False, verbose_name="Finalizada")
    
    class Meta:
        verbose_name='Agendamento'
        verbose_name_plural = 'Agendamentos'