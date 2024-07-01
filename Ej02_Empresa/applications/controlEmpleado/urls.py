from django.contrib import admin
from django.urls import path
from . import views


app_name = "controlEmpleado_app"

urlpatterns = [
    path(
        "listatodosempleados/", views.ListAllEmpleados.as_view(), name="empleados_all"
    ),
    path(
        "listapordepartamento/<valDpto>",
        views.ListByDptoEmpleado.as_view(),
        name="ver_pordpto",
    ),
    path(
        "listabusquedaempleado/",
        views.ListaEmpleadoByKword.as_view(),
        name="busqueda_empleado",
    ),
    path("listacursosxempleado", views.ListaDeCursosEmpleado.as_view()),
    path("verempleado/<int:pk>", views.DetalleEmpleado.as_view(), name="ver_empleado"),
    path("crearempleado/", views.CrearEmpleado.as_view(), name="crear_empleado"),
    path("successempleado/", views.SuccesView.as_view(), name="registro_correcto"),
    path("deleteempleado/", views.SuccesView2.as_view(), name="registro_eliminado"),
    path("signin/", views.Sesion.as_view(), name="signin"),
    path(
        "updateempleado/<int:pk>",
        views.UpdateEmpleado.as_view(),
        name="Actualizar_registro",
    ),
    path(
        "deleteempleado/<int:pk>",
        views.DeleteEmpleado.as_view(),
        name="Borrar_Registro",
    ),
    path("", views.InicioView.as_view(), name="inicio"),
]
