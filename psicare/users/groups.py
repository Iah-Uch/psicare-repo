from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# from .models import Administrator, Teacher, Secretary, Student

# def CreateManagerGroup():
#     new_group, created = Group.objects.get_or_create(name='new_group')
#     # Code to add permission to group ???
#     ct = ContentType.objects.get_for_model(Secretary)

#     # Now what - Say I want to add 'Can add project' permission to new_group?
#     permission = Permission.objects.create(codename='can_add_project',
#                                     name='Can add project',
#                                     content_type=ct)
#     new_group.permissions.add(permission)

# permission = Permission.objects.filter(codename__in=('view_student','add_student'))
# user_roles = ["Read only", "Maintainer"]
# for name in user_roles:
# 	Group.objects.create(name=name)
 
def GroupSetter(instance, group_name):
    try:
        my_group = Group.objects.get(name=group_name) 
        my_group.user_set.add(instance)
    except:
        pass
