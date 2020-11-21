from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cars/$', views.CarsListView.as_view(), name='cars'),
    url(r'^cars/(?P<pk>\d+)$', views.CarsDetailView.as_view(), name='cars-detail'),
    url('cars/new/', views.cars_new, name='cars_new'),
    path('cars/<int:pk>/edit/', views.cars_edit, name='cars_edit'),
    path('cars/<int:pk>/delete/', views.cars_delete, name='cars_delete'),
    ]
   