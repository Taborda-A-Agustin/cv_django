# Generated by Django 3.2.8 on 2021-11-02 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculumvitae', '0008_auto_20211101_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_finalizacion', models.DateField(blank=True, null=True)),
                ('nombre_trabajo', models.CharField(max_length=100)),
                ('descripción_trabajo', models.TextField(max_length=500)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trabajo', to='curriculumvitae.cv')),
            ],
        ),
    ]
