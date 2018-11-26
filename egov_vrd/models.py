from django.db import models
import uuid
import datetime


def get_uniqueId():
    current_month = str(datetime.date.today().month)
    current_year = str(datetime.date.today().year)

    return str(uuid.uuid4())[:8].upper() + '-' + current_month + current_year

class VehicleType(models.Model):
    type_code  = models.CharField('Type Code', max_length=5)
    type_name  = models.CharField('Type Name', max_length=100)

    def __str__(self):
        return self.type_name

ENGINE_SIZE = (
    ('1.2','1.2'),
    ('2.0','2.0'),
    ('3.0','3.0'),
    ('4.0','4.0'),
    ('5.0','5.0'),
    ('HD','Heavy Duty'),
)
TRANSMISSION = (
    ('Manuel','Manuel'),
    ('Automatic','Automatic'),
    ('Semi Auto','Semi Auto'),

)
FUEL_TYPE = (
    ('Gasoline','Gas'),
    ('Diesel','Dsl'),
    ('Electric','Ele'),
    ('Bio-Fuel','Bio'),
)
class TaxCategory(models.Model):
    tax_category_code = models.CharField('Tax Category Code', max_length=4)
    description = models.CharField('Description',max_length=100)

    def __str__(self):
        return self.tax_category_code

    class Meta:
        verbose_name_plural = 'Tax Categories'
        verbose_name = 'Tax Category'

class Owner(models.Model):
    owner_ref = models.CharField('Owner Reference',max_length=20, default=get_uniqueId)
    individual_owner_or_company = models.BooleanField('Individual or Company', default=False)
    owner_name = models.CharField('Organization Or Company Name', max_length=180, blank=True, null=True, help_text='Leave blank if Individual')
    first_name = models.CharField('First Name',max_length=100,blank=True, null=True)
    middle_name = models.CharField('Middle Name',max_length=100,blank=True, null=True)
    last_name = models.CharField('Last Name',max_length=100,blank=True, null=True)
    gender = models.CharField('Gender', max_length=1,choices=(('Female','F'),('Male','M'),('Not Specified','N')))
    date_of_birth = models.DateField('Date of Birth',blank=True)
    address = models.CharField('Address', max_length=100)
    city  = models.CharField('City', max_length=100)
    county  = models.CharField('County', max_length=100)
    telephone  = models.CharField('Telephone', max_length=20)
    mobile_number  = models.CharField('Mobile Number', max_length=20)
    email = models.EmailField('email',blank=True, default='')

    def __str__(self):
        return self.owner_ref
        
    class Meta:
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'
        db_table = 'vrd_owner'


class Vehicle(models.Model):
    vehicle_registration_ref = models.CharField('Vehicle Registration Reference',max_length=20, default=get_uniqueId)
    plate_number = models.CharField('Plate Number', max_length=10)
    vin_number = models.CharField('VIN Number', max_length=30)
    current_milage = models.DecimalField('Current Milage', max_digits=10, decimal_places=2, blank=True, null=True)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_color  = models.CharField('Vehicle Color', max_length=20)
    engine_size = models.CharField('Enigine Size', max_length=10, choices=ENGINE_SIZE, blank=True,null=True)
    transmission =  models.CharField('Transmission', max_length=10, choices=TRANSMISSION)
    fuel_type = models.CharField('Fuel Type', max_length=10, choices=FUEL_TYPE)
    tax_category_code = models.ForeignKey(TaxCategory, on_delete=models.CASCADE)



    def __str__(self):
        return self.plate_number

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'
        db_table = 'vrd_vehicle'

class VehicleOwnership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    recorded_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    ownership_transfer_date = models.DateField('Transfer on', blank=True)
    status = models.CharField('Status', max_length=10, default='Active')
    note = models.TextField()

    def __str__(self):
        return self.owner + '' + self.vehicle

    class Meta:
        unique_together = ['owner', 'vehicle']

