# Generated by Django 3.2 on 2021-05-23 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0002_pregunta_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='texto',
            field=models.CharField(max_length=2500),
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='respuesta',
            field=models.CharField(max_length=2500),
        ),
    ]