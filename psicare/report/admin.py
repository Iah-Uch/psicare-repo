from django.contrib import admin
from .models import Report
from users.models import Student
from django.utils.html import format_html
from .forms import ReportModelForm

class ReportAdmin(admin.ModelAdmin):
    form = ReportModelForm
    
    list_display = ('title','patient','res_student','finished',)
    list_filter = ('finished','created_at',)
    search_fields = ['title']


    save_as = True

    
    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser or request.user.check_group(["Alunos"]):
            return ( # Main viewing form fields  
                    ('Registro', {'fields': ('patient','title','report',)}),
                    ('Prontuário', {'fields': ('diagnosis','file', 'finished',)}),
                    )
        return ( # Main viewing form fields  
                    ('Registro', {'fields': ('patient','title','html_report',)}),
                    ('Prontuário', {'fields': ('diagnosis','file', 'finished',)}),
                    )
            
    
    def get_queryset(self, request): # Only returns current user's correspondent reports
        qs = super(ReportAdmin, self).get_queryset(request)
        
        if request.user.is_superuser or request.user.check_group(['Administradores']):
            return qs
        
        elif request.user.check_group(['Alunos']):
            return qs.filter(res_student=request.user)
        
        return qs.filter(res_student__in=Student.objects.filter(res_teacher=request.user))

    
admin.site.register(Report, ReportAdmin)