from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import logout_then_login, LoginView
from materias.views import *
from materias import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view, {'template_name':'login.html'}),
    path('',home, name='index'),
    
]
