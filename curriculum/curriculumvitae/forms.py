from django import forms
from .models import Cv


class CurriculumForm(forms.ModelForm):
	class Meta:
		model = Cv
		exclude = ["published_date", "created_date", "fotos"]
