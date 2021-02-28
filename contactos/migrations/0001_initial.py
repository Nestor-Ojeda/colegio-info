# Generated by Django 3.1.7 on 2021-02-28 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('codigo_pais', models.IntegerField(max_length=3)),
                ('codigo_area', models.IntegerField(max_length=5)),
                ('numero', models.IntegerField(max_length=15)),
            ],
        ),
    ]
