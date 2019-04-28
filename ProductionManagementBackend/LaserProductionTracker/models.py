from django.db import models


class LaserMachine(models.Model):
    name = models.CharField("Nickname", max_length=50, primary_key=True)
    brand = models.CharField(max_length=50)
    model_number = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50, unique=True)
    laser_area_length = models.IntegerField(max_length=3)
    laser_area_width = models.IntegerField(max_length=3)
    current_hours_used = models.IntegerField(max_length=6)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    hourly_depreciation_rate = models.FloatField()


class ProductionRun(models.Model):
    machine_used = models.ForeignKey('LaserMachine', on_delete=models.CASCADE)
    product_made = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity_made = models.IntegerField()
    time_started = models.DateTimeField()
    machine_time_used = models.DurationField(help_text="DD HH:MM:ss.uuuuuu")


class Product(models.Model):
    pass
