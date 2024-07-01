from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from applications.controlEmpleado.models import Empleado
from .models import Departamento

from .forms import NewDepartamentoForm
# Create your views here.

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'


    def form_valid(self, form):

        departamento = Departamento(
            nom = form.cleaned_data['nomDepa'],
            area = form.cleaned_data['areaDepa']
        )
        departamento.save()


        Empleado.objects.create(
            nom = form.cleaned_data['nomEmp'],
            tipo = '2',
            dpto = departamento
        )

        return super(NewDepartamentoView, self).form_valid(form)


class ListEmpleadoByDpto (ListView):
    template_name = 'departamento/ListDepartamento.html'
    model = Departamento
    context_object_name = 'Departamentos'
    ordering = 'nom'
