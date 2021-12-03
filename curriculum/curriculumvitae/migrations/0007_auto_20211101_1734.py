# Generated by Django 3.2.8 on 2021-11-01 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculumvitae', '0006_auto_20211101_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cv',
            old_name='habilidades1',
            new_name='nombre_habilidad1',
        ),
        migrations.RenameField(
            model_name='cv',
            old_name='habilidades2',
            new_name='nombre_habilidad2',
        ),
        migrations.RenameField(
            model_name='cv',
            old_name='habilidades3',
            new_name='nombre_habilidad3',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='habilidades4',
        ),
        migrations.AddField(
            model_name='cv',
            name='description_habilidad_1',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cv',
            name='description_habilidad_2',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cv',
            name='description_habilidad_3',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cv',
            name='description_habilidad_4',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cv',
            name='nombre_habilidad4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
