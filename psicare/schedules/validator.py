from django.core.exceptions import ValidationError
from django.utils import timezone

def date_validator(value):
    if value < timezone.now():
        raise ValidationError("A data do agendamento não pode estar no passado!")
    return value