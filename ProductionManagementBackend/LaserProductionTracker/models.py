from django.db import models
from datetime import datetime


class LaserMachine(models.Model):
    name = models.CharField("Nickname", max_length=50, primary_key=True, default='LaserX')
    brand = models.CharField(max_length=50, default='Trotec')
    model_number = models.CharField(max_length=50, default='Speedy400')
    serial_number = models.CharField(max_length=50, unique=True, default='000000')
    laser_area_depth = models.IntegerField(default=26)
    laser_area_width = models.IntegerField(default=48)
    current_hours_used = models.FloatField(max_length=15, default=0.0)
    value = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    hourly_depreciation_rate = models.FloatField(max_length=10, default=-0.21)

    def add_hours(self, number):
        self.current_hours_used += number

    def decrease_value(self, number):
        self.value -= number


class LaserProductionRun(models.Model):
    machine_used = models.ForeignKey('LaserMachine', on_delete=models.CASCADE, name='Machine')
    product_made = models.ForeignKey('Product', on_delete=models.CASCADE, name='Product')
    production_run_number = models.AutoField(primary_key=True)
    quantity_to_produce = models.IntegerField()
    laser_time_started = models.DateTimeField()
    laser_product_waste = models.IntegerField(default=0)
    laser_time_finished = models.DateTimeField()
    assembly_time_started = models.DateTimeField()
    assembly_product_waste = models.IntegerField(default=0)
    assembly_time_finished = models.DateTimeField()
    packaging_time_started = models.DateTimeField()
    packaging_product_waste = models.IntegerField(default=0)
    packaging_time_finished = models.DateTimeField()
    shrink_time_started = models.DateTimeField()
    shrink_bags_wasted = models.IntegerField(default=0)
    shrink_time_finished = models.DateTimeField()
    production_finished = models.BooleanField(default=False)
    total_quantity_produced = models.IntegerField(default=0)
    laser_job_is_claimed = models.BooleanField(default=False)
    assembly_job_is_claimed = models.BooleanField(default=False)
    packaging_job_is_claimed = models.BooleanField(default=False)
    shrink_job_is_claimed = models.BooleanField(default=False)
    laser_worker = models.CharField(max_length=100)
    assembly_worker = models.CharField(max_length=100)
    packaging_worker = models.CharField(max_length=100)
    shrinking_worker = models.CharField(max_length=100)

    # Laser Production Functions
    def start_laser(self):
        self.laser_time_started = datetime.now()

    def laser_waste(self, number):
        self.laser_product_waste += number

    def finish_laser(self):
        self.laser_time_finished = datetime.now()
    # ----------------------------------

    # Assembly Production Functions
    def start_assembly(self):
        self.assembly_time_started = datetime.now()

    def assembly_waste(self, number):
        self.assembly_product_waste += number

    def finish_assembly(self):
        self.assembly_time_finished = datetime.now()
    # ----------------------------------

    # Packaging Production Functions
    def start_packaging(self):
        self.packaging_time_started = datetime.now()

    def packaging_waste(self, number):
        self.packaging_product_waste += number

    def finish_packaging(self):
        self.packaging_time_finished = datetime.now()
    # ----------------------------------

    # Shrinking Production Functions
    def start_shrinking(self):
        self.shrink_time_started = datetime.now()

    def shrinking_waste(self, number):
        self.assembly_product_waste += number

    def finish_shrinking(self):
        self.shrink_time_finished = datetime.now()
    # ----------------------------------


class Product(models.Model):
    name = models.CharField(max_length=100, default='New Product', unique=True)
    sku = models.CharField(max_length=12, primary_key=True, default="000000000000")
    brand = models.CharField(max_length=100, default="PM Quilting & Laser Works, Inc")
    upc = models.BigIntegerField(default=0, unique=True)
    SLIP_STOP_CHOICES = (
        ('N', 'None'),
        ('1', '1" Tiny Strip'),
        ('3', '3" Small Strip'),
        ('6', '6" Medium Strip'),
        ('11A', '11" Half Strip for Mini AQSR'),
        ('13', '13" Large Strip'),
        ('23', '23.5" Half Strip for AQSR'),
    )
    slip_stop = models.CharField(max_length=3, choices=SLIP_STOP_CHOICES, default='N')
    HANG_TAB_CHOICES = (
        ('N', 'None'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('DL', 'Double Large'),
    )
    hang_tab = models.CharField(max_length=2, choices=HANG_TAB_CHOICES, default='N')
    has_cardboard = models.BooleanField(default=False)
    cardboard_length = models.FloatField(max_length=5, default=0.0)
    cardboard_width = models.FloatField(max_length=5, default=0.0)
    BAG_SIZE_CHOICES = (
        ('2', '2" Bag'),
        ('3', '3" Bag'),
        ('4', '4" Bag'),
        ('5', '5" Bag'),
        ('6', '6" Bag'),
        ('8', '8" Bag'),
        ('10', '10" Bag'),
        ('14', '14" Bag'),
        ('20', '20" Bag'),
        ('26', '26" Bag'),
    )
    bag_size = models.IntegerField(choices=BAG_SIZE_CHOICES, default=2)
    bag_length = models.FloatField(max_length=5, default=0.0)
    product_notes = models.TextField(max_length=5000, default="No notes at this time...")
