# Generated by Django 3.1.7 on 2021-02-28 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0001_initial'),
        ('personal', '0002_auto_20210228_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='telefono',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='telefono', to='contactos.contactos'),
        ),
    ]
