# Generated by Django 3.1.7 on 2021-02-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='edad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='telefono',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tutora',
            name='edad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tutora',
            name='telefono',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tutorb',
            name='edad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tutorb',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
