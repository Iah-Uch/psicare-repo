from django import forms
from cpf_field.forms import CPFFieldForm

class PatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['contact_number'].widget.attrs['class'] = "mask-phone"
        self.fields['cpf'].widget.attrs['class'] = "mask-cpf"