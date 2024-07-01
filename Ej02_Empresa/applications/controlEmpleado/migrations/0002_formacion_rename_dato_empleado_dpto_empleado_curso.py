# Generated by Django 4.2.5 on 2023-10-04 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlEmpleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=50, verbose_name='Curso ')),
            ],
            options={
                'verbose_name': 'Cursos',
                'verbose_name_plural': 'Cursos por Empleados',
            },
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='dato',
            new_name='dpto',
        ),
        migrations.AddField(
            model_name='empleado',
            name='curso',
            field=models.ManyToManyField(to='controlEmpleado.formacion'),
        ),
    ]
