# Generated by Django 3.1.7 on 2021-02-28 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
        ('personal', '0003_auto_20210228_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='personal',
            name='dni',
        ),
        migrations.RemoveField(
            model_name='personal',
            name='nombre',
        ),
        migrations.AddField(
            model_name='personal',
            name='persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pers', to='personas.persona'),
        ),
    ]
