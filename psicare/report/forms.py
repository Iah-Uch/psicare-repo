from django import forms
from patients.models import Patient
from .models import Report
from django_currentuser.middleware import get_current_authenticated_user

class ReportModelForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ReportModelForm, self).__init__(*args, **kwargs)
        if self.fields:
            self.fields['patient'].queryset = Patient.objects.filter(res_student=get_current_authenticated_user())# or something els