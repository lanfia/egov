from django.db import models
from egov_hr.models import MinistryAgency, Employee
import uuid
import datetime
from egov_core.models import Partner

COUNTY = (
    ('Bomi','Bomi County'),
    ('Bong','Bong County'),
    ('Gbpl','Gbarpolu County'),
    ('Grba','Grand Bassa County'),
    ('Grcm','Grand Cape Mount County'),
    ('Gcmt','Grand Gedeh County'),
    ('Grkr','Grand Kru County'),
    ('Lofa','Lofa County'),
    ('Marg','Margibi County'),
    ('Marl','Maryland County'), 
    ('Mont','Montserrado County'),
    ('Nimb','Nimba County'),
    ('Rivc','Rivercess County'),
    ('Rivg','River Gee County'),
    ('Sino','Sinoe County'),
) 

def get_uniqueId():
    current_month = str(datetime.date.today().month)
    current_year = str(datetime.date.today().year)

    return str(uuid.uuid4())[:8].upper() + '-' + current_month + current_year

class Category(models.Model):
    category_code = models.CharField('Category Code', max_length=5)
    category_name = models.CharField('Category Name', max_length=150)

    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Asset Category'
        db_table = 'vdr_category'


class Manufacturer(models.Model):
    manufacturer_code = models.CharField('Manfacturer Code', max_length=5, help_text='A three letters short code eg: TOY for Toyota')
    manufacturer_name = models.CharField('Manufacturer Name', max_length=150)

    def __str__(self):
        return self.manufacturer_name

    class Meta:
        verbose_name_plural = 'Manufacturers'
        verbose_name = 'Manufacturer'
        db_table = 'vrd_manufacturer'



class ManfacturerModel(models.Model):
    model_number = models.CharField('Model Number', max_length=150)
    manufacturer_name = models.ForeignKey(Manufacturer, on_delete = models.CASCADE)

    def __str__(self):
        return self.model_number

    class Meta:
        verbose_name_plural = 'Models'
        verbose_name = 'Manufacturer Model'
        db_table = 'ams_manufacturer_model'

class Asset(models.Model):
    DONATION_TYPE = (
        ('Loan','Loan'),
        ('Grant','Grant'),
    )
    gsa_asset_code = models.CharField('GSA Asset Code', max_length=15)
    asset_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    model_number = models.ForeignKey(ManfacturerModel, on_delete= models.CASCADE)
    serial_number = models.CharField('Serial Number',max_length=25)
    procurement_date = models.DateField('Procurement Date', blank=True, null=True)
    asset_value = models.DecimalField('Value of Asset', max_digits=10, decimal_places=2)
    asset_image = models.ImageField(default='default.png', upload_to='asset_pics')
    donated = models.BooleanField('Donated Vehicle ?', default=False)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, blank=True,null=True)
    donation_type = models.CharField('Donation Type',max_length=20, choices=DONATION_TYPE)
    status = models.CharField('Status', max_length=10, default='Active')
    note = models.TextField('Note')

    def __str__(self):
        return self.gsa_asset_code

    class Meta:
        verbose_name_plural = 'Assets'
        verbose_name = 'Asset'
        db_table = 'ams_asset'

class VehicleType(models.Model):
    type_code  = models.CharField('Type Code', max_length=5)
    type_name  = models.CharField('Type Name', max_length=100)

    def __str__(self):
        return type_name
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

class Vehicle(Asset):
 
    plate_number = models.CharField('Plate Number', max_length=10)
    vin_number = models.CharField('VIN Number', max_length=30)
    current_milage = models.DecimalField('Current Milage', max_digits=10, decimal_places=2, blank=True, null=True)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_color  = models.CharField('Vehicle Color', max_length=20)
    engine_size = models.CharField('Enigine Size', max_length=10, choices=ENGINE_SIZE, blank=True,null=True)
    transmission =  models.CharField('Transmission', max_length=10, choices=TRANSMISSION)
    fuel_type = models.CharField('Fuel Type', max_length=10, choices=FUEL_TYPE)



    def __str__(self):
        return self.plate_number

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'
        db_table = 'ams_vehicle'


class Location(models.Model):
    location = models.CharField('Location', max_length=150)
    county = models.CharField('County',max_length=5,choices=COUNTY)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name_plural = 'Locations'
        verbose_name = 'Location'
        db_table = 'ams_location'

class AssetTransfer(models.Model):
    transfer_ref = models.CharField('Transfer Reference',max_length=20, default=get_uniqueId)
    asset_transfer_request_ref = models.CharField('Trasfer Request Number', max_length=20)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    date_of_transfer = models.DateField('Transfer Date',blank=True, null=True)
    recorded_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    gol_ministry_agency_transfered_to = models.ForeignKey(MinistryAgency, on_delete=models.CASCADE, verbose_name='GOL Ministry/Agency Transfer To ?')
    authorized_by = models.ForeignKey(Employee,on_delete=models.CASCADE, verbose_name='Authorized By')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    status = models.CharField('Status', max_length=10, default='Transfered')
    note = models.TextField('Note')


    def __str__(self):
        return self.transfer_ref

    class Meta:
        verbose_name = 'Asset Transfer'
        verbose_name_plural = 'Asset Transfers'
        db_table = 'ams_asset_transfer'

class VehicleTransfer(models.Model):
    transfer_ref = models.CharField('Transfer Reference',max_length=20, default=get_uniqueId)
    asset_transfer_request_ref = models.CharField('Trasfer Request Number', max_length=20)
    asset = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date_of_transfer = models.DateField('Transfer Date',blank=True, null=True)
    recorded_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    gol_ministry_agency_transfered_to = models.ForeignKey(MinistryAgency, on_delete=models.CASCADE, verbose_name='GOL Ministry/Agency Transfer To ?')
    authorized_by = models.ForeignKey(Employee,on_delete=models.CASCADE, verbose_name='Authorized By')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    status = models.CharField('Status', max_length=10, default='Transfered')
    note = models.TextField('Note')


    def __str__(self):
        return self.transfer_ref

    class Meta:
        verbose_name = 'Vehicle Transfer'
        verbose_name_plural = 'Vehicle Transfers'
        db_table = 'ams_vehicle_transfer'


class AssetAssigned(models.Model):
    asset_assigned_ref  = models.CharField('Asset Assign Reference',max_length=20, default=get_uniqueId)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    #asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    date_of_transfer = models.DateField('Date of Transfer')
    recorded_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    transfer_slip_reference = models.CharField('Transfer Slip / Document Reference', max_length=20, blank=True, null=True)
    status = models.CharField('Status', max_length=10, default='Transfered')
    note = models.TextField('Note')


    def __str__(self):
        return asset_assigned_ref

    class Meta:
        verbose_name = 'Assign An Asset To'
        verbose_name_plural = ' Assets Assigned'
        db_table = 'ams_AssetAssigned'

class EmployeeAssetAssigned(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    AssetAssigned = models.ForeignKey(AssetAssigned, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200, blank=True,null=True)
    


    def __str__(self):
        return f'{self.employee} {self.asset}'

class Inventory(models.Model):
    inventory_number  = models.CharField('Asset Assign Reference',max_length=20, default=get_uniqueId)
    inventory_date = models.DateField('Inventory Date')
    name_ministry_agency = models.ForeignKey(MinistryAgency, on_delete=models.CASCADE)

    def __str__(self):
        return self.inventory_number

    class Meta:
        verbose_name_plural = 'Inventories'
        db_table = 'ams_inventory'
        verbose_name = 'Inventory'

class InventoryLog(models.Model):
    ASSET_STATE = (
        ('Dermaged','Dermaged'),
        ('Not Found','Not Found'),
        ('Good Order','Good Order'),

    )
    inventory_number = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    asset_state = models.CharField('State of Asset', max_length=20, choices=ASSET_STATE)
    comment = models.CharField(max_length=200, blank=True,null=True)
    asset_checked = models.BooleanField(default=False)
    log_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    current_milage = models.DecimalField('Current Milage', max_digits=10, decimal_places=2, blank=True, null=True)


    def __str__(self):
        return self.inventory_number

    class Meta:
        unique_together = ('inventory_number','asset')
        db_table = 'ams_inventory_log'
        verbose_name = 'Inventory Detail Log'
        verbose_name_plural = 'Inventory Logs'

class VehicleInventoryLog(models.Model):
    ASSET_STATE = (
        ('Dermaged','Dermaged'),
        ('Not Found','Not Found'),
        ('Good Order','Good Order'),

    )
    inventory_number = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    asset_state = models.CharField('State of Asset', max_length=20, choices=ASSET_STATE)
    comment = models.CharField(max_length=200, blank=True,null=True)
    asset_checked = models.BooleanField(default=False)
    log_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    current_milage = models.DecimalField('Current Milage', max_digits=10, decimal_places=2, blank=True, null=True)



    def __str__(self):
        return self.inventory_number

    class Meta:
        unique_together = ('inventory_number','vehicle')
        db_table = 'ams_vehicle_inventory_log'
        verbose_name = 'Vehicle Inventory Detail Log'
        verbose_name_plural = 'Inventory Logs'

