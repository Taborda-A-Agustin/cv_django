from .models import Cv
from .forms import CurriculumForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

def cv_list(request):
    CVS = Cv.objects.all().order_by('published_date')
    return render(request, 'curriculumvitae/cv_list.html', {'CVS': CVS})

def cv_detail(request, pk):
    cv_detail = get_object_or_404(Cv, pk=pk)
    return render(request, 'curriculumvitae/cv_detail.html', {'cv': cv_detail})


def cv_create(request):
    # si el pedido es POST tenemos que procesar la data del formulario
    if request.method == "POST":
        # Tenemos que instanciar el formulario con la informacion que nos envio el usuario
        form = CurriculumForm(request.POST)
        # Preguntamos si el formulario es valido
        if form.is_valid():
            # Procesamos la informacion
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = CurriculumForm()
    return render(request, 'curriculumvitae/cv_create.html', {"form": form})


def cv_update(request,pk):
    cv = Cv.objects.get(pk=pk)
    form = CurriculumForm(instance=cv)
    # si el pedido es POST tenemos que procesar la data del formulario
    if request.method == "POST":
        # Tenemos que instanciar el formulario con la informacion que nos envio el usuario
        form = CurriculumForm(request.POST, instance=cv)
        # Preguntamos si el formulario es valido
        if form.is_valid():
            # Procesamos la informacion
            form.save()
            return HttpResponseRedirect(reverse("cv_list"))
    return render(request, 'curriculumvitae/cv_create.html', {"form": form})




def thanks(request):
    return render(request, 'curriculumvitae/thanks.html')
