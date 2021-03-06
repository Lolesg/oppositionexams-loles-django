# Generated by Django 3.2 on 2021-05-01 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(blank=True, max_length=250, null=True, unique=True, verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Categría',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_categoria', models.CharField(blank=True, max_length=250, null=True, verbose_name='Sub-Categoría')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='examenes.categoria', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Sub-Categoría',
                'verbose_name_plural': 'Sub-Categorias',
            },
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('numero_de_preguntas', models.IntegerField()),
                ('tiempo', models.IntegerField(help_text='Duración del examen en minutos')),
                ('puntuacion_para_pasar', models.IntegerField(help_text='Puntuación en % necesaria para aprobar')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='examenes.categoria', verbose_name='Categoría')),
                ('sub_categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='examenes.subcategoria', verbose_name='Sub-Categoría')),
            ],
            options={
                'verbose_name_plural': 'Examenes',
            },
        ),
    ]
