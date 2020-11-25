from django.shortcuts import render
from django.utils import timezone, dateformat
from .models import Cars
from .forms import CarsForm

def index(request):

    num_cars=Cars.objects.all().count()
    name_cars=Cars.objects.all()
    
    return render(
        request,
        'index.html',
        context={'num_cars':num_cars, 'name_cars':name_cars},
    )

from django.views import generic




class CarsListView(generic.ListView):
    model = Cars

class CarsDetailView(generic.DetailView):
    model = Cars

from datetime import datetime
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format
def cars_filter(request):
    
    if request.method == "POST":
        form = CarsForm(request.POST)
        name_cars = Cars.objects.filter(date_on__isnull=True, date_on__range=(request.POST['date_on'], request.POST['date_off']))
        return render(
        request,
        'catalog/cars_filter.html',
        context={'form':form, 'name_cars':name_cars},
        )
    else:
        name_cars=Cars.objects.all()
        form = CarsForm()
    return render(
        request,
        'catalog/cars_filter.html',
        context={'form':form, 'name_cars':name_cars},
    )


from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
def cars_new(request):
    if request.method == "POST":
        form = CarsForm(request.POST)
        cars = form.save(commit=False)
        cars.save()

        return HttpResponseRedirect(reverse('cars') )
    else:
        form = CarsForm()
    return render(request, 'catalog/cars_edit.html', {'form': form })

def cars_edit(request, pk):
    post = get_object_or_404(Cars, pk=pk)
    if request.method == "POST":
        form = CarsForm(request.POST, instance=post)
        if form.is_valid():
            post.save()
            return HttpResponseRedirect(reverse('cars') )
    else:
        form = CarsForm(instance=post)
    return render(request, 'catalog/cars_edit.html', {'form': form})

def cars_delete(request, pk):
    post = get_object_or_404(Cars, pk=pk)
    post.delete()
    num_cars=Cars.objects.all().count()
    name_cars=Cars.objects.all()
    
    return HttpResponseRedirect(reverse('cars') )
