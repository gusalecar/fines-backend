# Generated by Django 3.2.6 on 2021-09-03 03:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=8)),
                ('domicilio', models.TextField()),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CENS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=25)),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='CicloLectivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Coordinador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=8)),
                ('domicilio', models.TextField()),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cursada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.SmallIntegerField(choices=[(1, 'Activa'), (2, 'Inactiva'), (3, 'Transferido'), (4, 'Aprobada')])),
                ('nota_final', models.FloatField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ige', models.IntegerField()),
                ('jornada', models.SmallIntegerField(choices=[(1, 'Simple'), (2, 'Doble')])),
                ('turno', models.SmallIntegerField(choices=[(1, 'Mañana'), (2, 'Tarde'), (3, 'Vespertino')])),
                ('ciclo_lectivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ciclolectivo')),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=8)),
                ('domicilio', models.TextField()),
                ('titulo', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('tipo', models.PositiveSmallIntegerField(choices=[(1, 'Examen'), (2, 'Recuperatorio'), (3, 'TP')])),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.curso')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuatrimestre', models.PositiveSmallIntegerField(choices=[(1, 'Primero'), (2, 'Segundo')])),
                ('nivel', models.PositiveSmallIntegerField()),
                ('nombre', models.CharField(max_length=15)),
                ('carga_horaria', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=25)),
                ('nombre', models.CharField(max_length=25)),
                ('cens', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cens')),
            ],
        ),
        migrations.CreateModel(
            name='Referente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=8)),
                ('domicilio', models.TextField()),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('cursada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cursada')),
                ('evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.evaluacion')),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.SmallIntegerField(choices=[(1, 'Lunes'), (2, 'Martes'), (3, 'Miércoles'), (4, 'Jueves'), (5, 'Viernes')])),
                ('hora', models.TimeField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.curso')),
            ],
        ),
        migrations.CreateModel(
            name='DocenteCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desde', models.DateField()),
                ('hasta', models.DateField()),
                ('revista', models.SmallIntegerField(choices=[(1, 'Titular'), (2, 'Suplente')])),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.curso')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.docente')),
            ],
        ),
        migrations.AddField(
            model_name='docente',
            name='materias',
            field=models.ManyToManyField(to='api.Materia'),
        ),
        migrations.AddField(
            model_name='docente',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='curso',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.materia'),
        ),
        migrations.AddField(
            model_name='curso',
            name='sede',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sede'),
        ),
        migrations.AddField(
            model_name='cursada',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.curso'),
        ),
        migrations.CreateModel(
            name='CoordinadorCENS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio_actividad', models.DateField()),
                ('fin_actividad', models.DateField()),
                ('cens', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cens')),
                ('coordinador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.coordinador')),
            ],
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('descripcion', models.TextField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.curso')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presente', models.BooleanField()),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clase')),
                ('cursada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cursada')),
            ],
        ),
    ]