from django.forms import ModelForm
from .models import LaserProductionRun


class CreateProductionRunForm(ModelForm):
    model = LaserProductionRun
    fields = ['Machine',
              'Product',
              'quantity_to_produce',
              ]
