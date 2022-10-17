from django.contrib import admin
from .models import Patient

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    model = Patient
    
    list_display = ('name', 'cpf','email', 'treatment_bg',)
    list_filter = ('discharged',)
    
    fieldsets = ( # Creation form fields
        ('Informações Pessoais', {'fields': ('name','cpf','address','age','sex','place_of_birth','nationality',
                                            'marital_status','family_wage', 'religion', 'profession',
                                            'scholar_affiliation','uni_affiliated',)}),
        
        ('Contato', {'fields': ('email','contact',)}),
        
        ('Tratamento', {'description': "Informações sobre o Status do Tratamento",
            'fields': ('treatment_bg','treatment_ed','discharged',),
                        'classes': ('collapse', 'collapse-closed'),}
         )
    )
    
    search_fields = ('name','cpf','email',)
    ordering = ('name',)

admin.site.register(Patient, PatientAdmin)