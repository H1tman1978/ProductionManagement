from django.template.loader import get_template
from django.http import HttpResponse


# Create your views here.
def index(request):
    html = get_template('production_index.html')
    return HttpResponse(html)


def start_production_run(request):
    return HttpResponse("You have reached the start production run page. Currently under construction")


def form_submitted(request):
    return HttpResponse("Your form has been submitted successfully. (Page under construction)")


def view_active_production_runs(request):
    return HttpResponse("Here's a list of all unfinished production runs. (Page under construction)")


def do_laser_work(request):
    return HttpResponse("Working on a Laser Page (Under Construction)")


def do_assembly(request):
    return HttpResponse("Working on Assembly Page (Under Construction)")


def do_packaging(request):
    return HttpResponse("Working on Packaging Page (Under Construction)")


def do_shrinking(request):
    return HttpResponse("Working on Shrinking Page (Under Construction)")
