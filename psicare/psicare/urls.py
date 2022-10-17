from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]

# Admin Page Configs
admin.site.site_header = "Psicare"
admin.site.site_title = "Psicare"
admin.site.index_title = "Bem Vindo!"