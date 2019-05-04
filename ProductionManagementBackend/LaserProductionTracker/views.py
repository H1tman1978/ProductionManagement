from django.template import RequestContext
from django.shortcuts import render
from .models import active_jobs, all_jobs, LaserProductionRun


# Create your views here.
def production_index(request):
    return render(request, 'production_index.html')


def view_all_jobs(request):
    context = RequestContext(request)
    jobs = all_jobs()
    return render(request, 'all_jobs.html', {'jobs': jobs}, context)


def form_submitted(request):
    return render(request, 'form_submitted.html')


def view_active_jobs(request):
    context = RequestContext(request)
    jobs = active_jobs()
    return render(request, 'view_active_jobs.html', {'jobs': jobs}, context)


def my_jobs(request):
    context = RequestContext(request)
    laser_jobs = LaserProductionRun.objects.all().filter(laser_worker=request.user).filter(
        laser_time_finished__isnull=True)
    assembly_jobs = LaserProductionRun.objects.all().filter(assembly_worker=request.user).filter(
        assembly_time_finished__isnull=True)
    packaging_jobs = LaserProductionRun.objects.all().filter(packaging_worker=request.user).filter(
        packaging_time_finished__isnull=True)
    shrinking_jobs = LaserProductionRun.objects.all().filter(shrinking_worker=request.user).filter(
        shrink_time_finished__isnull=True)
    return render(request, 'my_jobs.html', {'laser_jobs': laser_jobs, 'assembly_jobs': assembly_jobs,
                                            'packaging_jobs': packaging_jobs, 'shrinking_jobs': shrinking_jobs},
                  context)


def do_laser_work(request):
    context = RequestContext(request)
    laser_jobs = LaserProductionRun.objects.all().filter(laser_worker__isnull=True)
    return render(request, 'do_laser_work.html', {'laser_jobs': laser_jobs}, context)


def do_assembly(request):
    context = RequestContext(request)
    assembly_jobs = LaserProductionRun.objects.all().filter(assembly_worker__isnull=True)
    return render(request, 'do_assembly.html', {'assembly_jobs': assembly_jobs}, context)


def do_packaging(request):
    context = RequestContext(request)
    packaging_jobs = LaserProductionRun.objects.all().filter(packaging_worker__isnull=True)
    return render(request, 'do_packaging.html', {'packaging_jobs': packaging_jobs}, context)


def do_shrinking(request):
    context = RequestContext(request)
    shrinking_jobs = LaserProductionRun.objects.all().filter(shrinking_worker__isnull=True)
    return render(request, 'do_assembly.html', {'shrinking_jobs': shrinking_jobs}, context)
