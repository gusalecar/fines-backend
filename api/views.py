from rest_framework import viewsets

from . import serializers, models

class AlumnoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.AlumnoSerializer
    queryset = models.Alumno.objects.all()

class AsistenciaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.AsistenciaSerializer
    queryset = models.Asistencia.objects.all()

class CENSViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.CENSSerializer
    queryset = models.CENS.objects.all()

class CicloLectivoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.CicloLectivoSerializer
    queryset = models.CicloLectivo.objects.all()

class ClaseViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.ClaseSerializer
    queryset = models.Clase.objects.all()

class CoordinadorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.CoordinadorSerializer
    queryset = models.Coordinador.objects.all()

class CoordinadorCENSViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.CoordinadorCENSSerializer
    queryset = models.CoordinadorCENS.objects.all()

class CursadaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.CursadaSerializer
    queryset = models.Cursada.objects.all()

class CursoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.CursoSerializer
    queryset = models.Curso.objects.all()

class DocenteViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.DocenteSerializer
    queryset = models.Docente.objects.all()

class DocenteCursoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.DocenteCursoSerializer
    queryset = models.DocenteCurso.objects.all()

class EvaluacionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.EvaluacionSerializer
    queryset = models.Evaluacion.objects.all()

class MateriaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.MateriaSerializer
    queryset = models.Materia.objects.all()

class NotaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.NotaSerializer
    queryset = models.Nota.objects.all()

class SedeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.SedeSerializer
    queryset = models.Sede.objects.all()
