from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('start_production_run/', views.start_production_run, name='start production'),
    path('form_submitted/', views.form_submitted, name='form submitted'),
    path('active_production/', views.view_active_production_runs, name='active production'),
]