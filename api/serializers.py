from rest_framework import serializers

from . import models

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alumno
        fields = '__all__'

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Asistencia
        fields = '__all__'

class CENSSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CENS
        fields = '__all__'

class CicloLectivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CicloLectivo
        fields = '__all__'

class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clase
        fields = '__all__'

class CoordinadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Coordinador
        fields = '__all__'

class CoordinadorCENSSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CoordinadorCENS
        fields = '__all__'

class CursadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cursada
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Curso
        fields = '__all__'

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Docente
        fields = '__all__'

class DocenteCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DocenteCurso
        fields = '__all__'

class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Evaluacion
        fields = '__all__'

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Materia
        fields = '__all__'

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Nota
        fields = '__all__'

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sede
        fields = '__all__'
