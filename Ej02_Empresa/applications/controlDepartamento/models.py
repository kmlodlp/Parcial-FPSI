from django.db import models

# Create your models here.
class Departamento(models.Model):
    nom = models.CharField('Nombre Departamento', max_length=50, unique=True)
    area = models.CharField('Area', max_length=30, blank=True, null=True)
    estado = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = 'Departamentos'
        verbose_name_plural = 'Departamentos Empresas'
        ordering= ['nom']
        unique_together = ('nom','area')

    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nom + ' - ' + self.area + ' - ' + str(self.estado)
