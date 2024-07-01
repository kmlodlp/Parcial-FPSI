from django.db import models
from applications.controlDepartamento.models import Departamento

# Create your models here.
#  

class Formacion(models.Model):
    curso = models.CharField("Curso ", max_length=50)

    class Meta:
        verbose_name = 'Cursos'
        verbose_name_plural = 'Cursos por Empleados'

    
    def __str__(self) -> str:
        return str(self.id)+' - '+self.curso


class Empleado(models.Model):
    Tipo_Choice = {
        ('1','Medio Tiempo'),
        ('2', 'Tiempo Completo'),
        ('3', 'Otro'),
    }

    nom = models.CharField("Nombre Empleado", max_length=50, unique=True)
    tipo = models.CharField("Tipo de Contrato", max_length=1 , choices=Tipo_Choice )
    dpto = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    curso = models.ManyToManyField(Formacion)

    def __str__(self) ->str:
        return str(self.id)+' - '+self.nom+' - '+self.tipo+' - '+str(self.dpto)
    
