from django.conf import settings
from django.db import models

class Persona(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dni = models.CharField(max_length=8)
    domicilio = models.TextField()

    class Meta:
        abstract = True

class Alumno(Persona):
    pass

class Coordinador(Persona):
    pass

class Referente(Persona):
    pass

class Docente(Persona):
    titulo = models.TextField()
    materias = models.ManyToManyField('Materia')

class Materia(models.Model):
    CUATRIMESTRE = (
        (1, 'Primero'),
        (2, 'Segundo'),
    )

    cuatrimestre = models.PositiveSmallIntegerField(choices=CUATRIMESTRE)
    nivel = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=15)
    carga_horaria = models.FloatField()

class CicloLectivo(models.Model):
    año = models.IntegerField()

class CENS(models.Model):
    direccion = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)

class CoordinadorCENS(models.Model):
    inicio_actividad = models.DateField()
    fin_actividad = models.DateField()
    coordinador = models.ForeignKey(Coordinador, on_delete=models.CASCADE)
    cens = models.ForeignKey(CENS, on_delete=models.CASCADE)

class Sede(models.Model):
    direccion = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)
    cens = models.ForeignKey(CENS, on_delete=models.CASCADE)
    
class Curso(models.Model):
    JORNADA = (
        (1, 'Simple'),
        (2, 'Doble'),
    )
    TURNO = (
        (1, 'Mañana'),
        (2, 'Tarde'),
        (3, 'Vespertino'),
    )

    ige = models.IntegerField()
    jornada = models.SmallIntegerField(choices=JORNADA)
    turno = models.SmallIntegerField(choices=TURNO)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    ciclo_lectivo = models.ForeignKey(CicloLectivo, on_delete=models.CASCADE)

class DocenteCurso(models.Model):
    REVISTA = (
        (1, 'Titular'),
        (2, 'Suplente'),
    )
    
    desde = models.DateField()
    hasta = models.DateField()
    revista = models.SmallIntegerField(choices=REVISTA)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class Horario(models.Model):
    DIA = (
        (1, 'Lunes'),
        (2, 'Martes'),
        (3, 'Miércoles'),
        (4, 'Jueves'),
        (5, 'Viernes'),
    )

    dia = models.SmallIntegerField(choices=DIA)
    hora = models.TimeField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class Cursada(models.Model):
    ESTADO = (
        (1, 'Activa'),
        (2, 'Inactiva'),
        (3, 'Transferido'),
        (4, 'Aprobada'),
    )

    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estado = models.SmallIntegerField(choices=ESTADO)
    nota_final = models.FloatField()

class ClaseAbstracta(models.Model):
    fecha = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Evaluacion(ClaseAbstracta):
    EVALUACION = (
        (1, 'Examen'),
        (2, 'Recuperatorio'),
        (3, 'TP'),
    )

    tipo = models.PositiveSmallIntegerField(choices=EVALUACION)

class Clase(ClaseAbstracta):
    descripcion = models.TextField()

class Nota(models.Model):
    valor = models.FloatField()
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    cursada = models.ForeignKey(Cursada, on_delete=models.CASCADE)

class Asistencia(models.Model):
    presente = models.BooleanField()
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    cursada = models.ForeignKey(Cursada, on_delete=models.CASCADE)
