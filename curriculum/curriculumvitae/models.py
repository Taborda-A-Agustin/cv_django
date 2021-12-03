from django.db import models
from django.utils import timezone

# Create your models here.

class Cv(models.Model):
	fotos = models.ImageField(upload_to="fotos", null=True)
	nombre_completo = models.CharField(max_length=50)
	nacimiento = models.DateField(
		default=timezone.now)
	domicilio = models.CharField(max_length=80)
	email = models.EmailField(max_length=80)
	nombre_hobbie_1= models.TextField(max_length=100)
	description_hobbie_1 = models.TextField(max_length=100)
	nombre_hobbie_2 = models.TextField(max_length=100)
	description_hobbie_2 = models.TextField(max_length=100)
	nombre_hobbie_3 = models.TextField(max_length=100)
	description_hobbie_3 = models.TextField(max_length=100)
	yo_soy = models.CharField(max_length=50)
	yo_soy_description = models.TextField(max_length=500)
	profesion = models.TextField(max_length=100)
	experiencia = models.CharField(max_length=1000)
	formacionAcademica = models.TextField(max_length=500)
	cursos = models.TextField(max_length=1000)
	telefono = models.CharField(max_length=20)
	localidad = models.TextField(max_length=50)
	webPage = models.CharField(max_length=100)
	nombre_habilidad_1 = models.CharField(max_length=50)
	description_habilidad_1 = models.TextField(max_length=100, blank=True, null= True)
	nombre_habilidad_2 = models.CharField(max_length=50)
	description_habilidad_2 = models.TextField(max_length=100, blank=True, null= True)
	nombre_habilidad_3 = models.CharField(max_length=50)
	description_habilidad_3 = models.TextField(max_length=100, blank=True, null= True)
	nombre_habilidad_4 = models.CharField(max_length=50, blank=True, null= True)
	description_habilidad_4 = models.TextField(max_length=100, blank=True, null= True)
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.nombre_completo


class Trabajos(models.Model):
	job = models.ForeignKey(to=Cv, related_name='trabajo', on_delete=models.CASCADE)
	fecha_inicio = models.DateField()
	fecha_finalizacion = models.DateField(blank=True, null=True)
	nombre_trabajo = models.CharField(max_length=100)
	descripcion_trabajo = models.TextField(max_length=500)

	def default_trabajo(self):
		if not self.fecha_finalizacion:
			return f'{self.fecha_inicio} - Actualidad'
		return f'{self.fecha_inicio} - {self.fecha_finalizacion}'
		