from django.contrib import admin
from django.db import models
from django.forms import TextInput

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.utils.crypto import get_random_string
from authtools.admin import NamedUserAdmin

from .forms import CustomUserCreationForm, GroupAdminForm
from .models import CustomUser, Student, Secretary, Teacher
from django.contrib.auth.models import Group

User = get_user_model()


# Unregister the original Group admin.
admin.site.unregister(Group)

class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm

    filter_horizontal = ['permissions']

admin.site.register(Group, GroupAdmin)


class UserAdmin(NamedUserAdmin): # Manages general user creation on admin interface
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete':'off', 'class':'collapse'})},
    }
    add_form = CustomUserCreationForm
    
    list_display = ('name', 'cpf','email', 'is_active',)
    list_filter = ('is_active','groups')
    
    fieldsets = ( # Main form fields
        (None, {'fields': ('name','cpf','email', 'password')}),
        ('Permissões', {'fields': ('is_active',)}),
    )
    add_fieldsets = ( # Creation form fields
        (None, {
            'classes': ('wide',),
            'fields': ('name','cpf','email')
        }),
        ('Permissões', {
            'fields': ('is_active',),
        }),
        ('Senha', {
            'description': "Opcionalmente, pode-se definir uma senha aqui.",
            'fields': ('password1', 'password2'),
            'classes': ('collapse', 'collapse-closed'),
            
        }),
    )
    
    def save_model(self, request, obj, form, change): # Saves user and sends a password setting email
        obj.is_staff = True
        if not change and (not form.cleaned_data['password1'] or not obj.has_usable_password()):
            # Django's PasswordResetForm won't let us reset an unusable
            # password. We set it above super() so we don't have to save twice.
            obj.set_password(get_random_string(length=8))
            obj.save()
            reset_password = True
        else:
            reset_password = False

        super(UserAdmin, self).save_model(request, obj, form, change)

        if reset_password:
            reset_form = PasswordResetForm({'email': obj.email})
            assert reset_form.is_valid()
            reset_form.save(
                request=request,
                use_https=request.is_secure(),
            )
    
    search_fields = ('name','cpf','email',)
    ordering = ('name',)

admin.site.register(CustomUser, UserAdmin) # Registers ALL Users

class StudentAdmin(UserAdmin): # Inherits UserAmin and sets model fields
    add_form = CustomUserCreationForm
    
    list_display = ('name', 'cpf','email','term', 'is_active',)
    list_filter = ('is_active',)
    
    fieldsets = ( # Main form fields
        (None, {'fields': ('name','cpf','email','registration','term','active_class', 'password')}),
        ('Permissions', {'fields': ( 'is_active',)}),
    )
    add_fieldsets = ( # Creation form fields
        (None, {
            'classes': ('wide',),
            'fields': ('name','cpf','email','registration','term','active_class')
        }),
        ('Permissões', {
            'fields': ('is_active',),
        }),
        ('Senha', {
            'description': "Opcionalmente, pode-se definir uma senha aqui.",
            'fields': ('password1', 'password2'),
            'classes': ('collapse', 'collapse-closed'),
        }),
    )
    
    def save_model(self, request, obj, form, change): # Saves user and sends a password setting email
        obj.is_staff = True
        if not change and (not form.cleaned_data['password1'] or not obj.has_usable_password()):
            # Django's PasswordResetForm won't let us reset an unusable
            # password. We set it above super() so we don't have to save twice.
            
            obj.set_password(get_random_string(length=8))
            obj.save()
            reset_password = True
        else:
            reset_password = False

        super(StudentAdmin, self).save_model(request, obj, form, change)

        if reset_password:
            reset_form = PasswordResetForm({'email': obj.email})
            assert reset_form.is_valid()
            reset_form.save(
                request=request,
                use_https=request.is_secure(),
            )
    
    search_fields = ('name','cpf','email', 'term', 'registration')

admin.site.register(Student, StudentAdmin) # Registers Students 

class SecretaryAdmin(UserAdmin): # Inherits UserAmin
    list_filter = ('is_active',)

admin.site.register(Secretary, SecretaryAdmin) # Registers Secretaries

class TeacherAdmin(UserAdmin): # Inherits UserAmin
    list_filter = ('is_active',)

admin.site.register(Teacher, TeacherAdmin) # Registers Teachers