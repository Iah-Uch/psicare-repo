from django.contrib import admin

from .forms import PatientForm
from .models import Patient
from users.models import Student

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    form = PatientForm
    list_display = ('name', 'email', 'res_student', 'treatment_bg',)
    list_filter = ('discharged','treatment_bg',)
    
    fieldsets = ( # Creation form fields
        ('Informações Pessoais', {'fields': ('name','cpf','address','age','sex',('nationality','place_of_birth'),
                                            'marital_status','family_wage', 'religion', ('profession', 'is_employee'),
                                            ('scholar_affiliation','uni_affiliated'),)}),
        
        ('Contato', {'fields': ('email','contact_number',)}),
        
        ('Tratamento', {'description': "Informações sobre o Status do Tratamento",
            'fields': ('res_student','treatment_bg','treatment_ed','discharged',),
                        'classes': ('collapse', 'expanded'),}
         )
    )
    
    search_fields = ('name','cpf','email',)
    ordering = ('name',)

    def get_queryset(self, request): # Only returns current user's correspondent students
        qs = super(PatientAdmin, self).get_queryset(request)
        if request.user.is_superuser or request.user.check_group(['Administradores','Secretárias']):
            return qs
        elif request.user.check_group(['Alunos']):
            return qs.filter(res_student=request.user)
        
        return qs.filter(res_student__in=Student.objects.filter(res_teacher=request.user))
    
    class Media:
        js = ("https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js",
              "https://cdnjs.cloudflare.com/ajax/libs/jquery.inputmask/5.0.7/jquery.inputmask.min.js",
              "custom.js")

admin.site.register(Patient, PatientAdmin)