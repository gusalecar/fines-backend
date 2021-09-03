from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('alumnos', views.AlumnoViewSet, 'alumnos')
router.register('asistencias', views.AsistenciaViewSet, 'asistencias')
router.register('cens', views.CENSViewSet, 'cens')
router.register('cicloslectivos', views.CicloLectivoViewSet, 'cicloslectivos')
router.register('clases', views.ClaseViewSet, 'clases')
router.register('coordinadores', views.CoordinadorViewSet, 'coordinadores')
router.register('coordinadorcens', views.CoordinadorCENSViewSet, 'coordinadorcens')
router.register('cursadas', views.CursadaViewSet, 'cursadas')
router.register('cursos', views.CursoViewSet, 'cursos')
router.register('docentes', views.DocenteViewSet, 'docentes')
router.register('docentecursos', views.DocenteCursoViewSet, 'docentecursos')
router.register('evaluaciones', views.EvaluacionViewSet, 'evaluaciones')
router.register('materias', views.MateriaViewSet, 'materias')
router.register('notas', views.NotaViewSet, 'notas')
router.register('sedes', views.SedeViewSet, 'sedes')

urlpatterns = [
    path('', include(router.urls)),
]
