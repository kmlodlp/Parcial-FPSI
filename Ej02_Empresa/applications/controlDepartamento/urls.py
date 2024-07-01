from django.contrib import admin 
from django.urls import path
from . import views 

app_name = 'controlDepartamento_app'

urlpatterns = [
    path('newdepartamento/', views.NewDepartamentoView.as_view(), name='nuevodepartamento'),
    path('listaDepartamentos/', views.ListEmpleadoByDpto.as_view(), name='lista_Departamento'),
]