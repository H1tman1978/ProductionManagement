from django.urls import path

from .views import *

urlpatterns = [
    path('', production_index, name='production_index'),
    path('all_jobs/', view_all_jobs, name='all jobs'),
    path('job/new/form_submitted/', form_submitted, name='form submitted'),
    path('job/active/', view_active_jobs, name='active jobs'),
    path('job/needs_laser/', do_laser_work, name='laser jobs'),
    path('job/needs_assembly/', do_assembly, name='assembly jobs'),
    path('job/needs_packaging/', do_packaging, name='packaging jobs'),
    path('job/needs_shrinking/', do_shrinking, name='shrinking jobs'),
    path('jobs/my_jobs/', my_jobs, name='my jobs'),
]
