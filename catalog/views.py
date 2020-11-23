from django.shortcuts import render
from django.utils import timezone, dateformat
# Create your views here.
from .models import Cars
# from .models import CarsInstance
from .forms import CarsForm

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
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
        
        name_cars=Cars.objects.all()
        form = CarsForm(request.POST)
        # d_on = request.POST['date_on']
        # d_off = request.POST['date_off']
        # d_on1 = DateFormat(d_on)
        # d_off2 = DateFormat(d_off)
        # d_on1.format('Y-m-d')
        # df2.format('Y-m-d')
        n = Cars.objects.filter(date_on__isnull=True, date_on__range=(request.POST['date_on'], request.POST['date_off']))
        print(n)
        # cars = CarsForm(request.POST)
        # cars.date_on = timezone.now()
        # cars.name =  request.user

        # cars.save()

        # return HttpResponseRedirect(reverse('cars') )
        # # return redirect ('catalog/cars_edit.html', pk=post.pk)
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
        cars = CarsForm(request.POST)
        print (request.POST['date_on'])
        # cars.date_on = request.POST['date_on']
        # cars.name =  request.POST['name']

        cars.save()

        return HttpResponseRedirect(reverse('cars') )
		# return redirect ('catalog/cars_edit.html', pk=post.pk)
    else:
        form = CarsForm()
    return render(request, 'catalog/cars_edit.html', {'form': form })

def cars_edit(request, pk):
    post = get_object_or_404(Cars, pk=pk)
    if request.method == "POST":
        form = CarsForm(request.POST, instance=post)
        if form.is_valid():
            # post = form.save(commit=False)
            # post.name = request.name
            # post.published_date = timezone.now()
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
