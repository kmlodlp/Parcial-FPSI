from django.contrib import admin
from .models import Empleado, Formacion
#from .models import Formacion

class EmpleadoAdmin (admin.ModelAdmin):
    list_display = (
        'nom', 
        'dpto',
        'tipo',
        'salario'
    )
    def salario(self, obj):
        if (str((obj.tipo))=='1'):
            return 'SMLV 1.5'
        elif(str((obj.tipo))=='2'):
            return 'SMLV 3'

    search_fields = ('nom',)
    list_filter = ('tipo',)
    filter_horizontal = ('curso',)


# Register your models here.
admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Formacion)