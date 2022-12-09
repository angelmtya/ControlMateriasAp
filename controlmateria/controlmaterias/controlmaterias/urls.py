from django.contrib import admin
from django.urls import path
from materias.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('login/', )
    path('',home),
]
