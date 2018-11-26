from django.db import models
import uuid
import datetime

def get_uniqueId():
    current_month = str(datetime.date.today().month)
    current_year = str(datetime.date.today().year)

    return str(uuid.uuid4())[:8].upper() + '-' + current_month + current_year
TITLE = (('Mr','Mr'),('Miss','Miss'),)

COUNTY = (
    ('Bomi','Bomi'),
    ('Bong','Bong'),
    ('Gbar','Gbarpolu'),
    ('GBas','Grand Bassa'),
    ('Cape','Grand Cape Mount'),
    ('Gged','Grand Gedeh'),
    ('Gkru','Grand Kru'),
    ('Lofa','Lofa'),
    ('Marg','Margibi'),
    ('Mary','Maryland'),
    ('Mont','Montserrado'),('Nimb','Nimba'),('Rces','Rivercess'),('Rgee','River Gee'),('Sino','Sinoe'),
)

GENDER =(('F','Female'),('M','Male'),)

class Department(models.Model):
    department_code = models.CharField(verbose_name='Department Code', max_length=5, unique=True)
    department_name = models.CharField(verbose_name='Department Name', max_length=100)
    

    def __str__(self):
        return self.department_name

    class Meta:
        verbose_name_plural = 'Departments'

class MinistryAgency(models.Model):
    entity_code = models.CharField(max_length=5, verbose_name='Entity Code')
    entity_name = models.CharField(max_length=100, verbose_name='Ministry / Agency Name')

    def __str__(self):
        return self.entity_code

    class Meta:
        verbose_name_plural = 'Gov Entities'
        verbose_name = 'Ministry / Angency'

class Job(models.Model):
    job_ref = models.CharField('Job Reference', max_length=100)
    title = models.CharField('Job Title', max_length=150)

    def __str_(self):
        return self.title



class Employee(models.Model):
    employee_ref = models.CharField(max_length=15, primary_key=True, default=get_uniqueId, verbose_name='Employee Code')
    title = models.CharField(max_length=10, verbose_name='Title', choices=TITLE)
    first_name = models.CharField(max_length=80, verbose_name='First Name')
    middle_name = models.CharField(max_length=80, verbose_name='Middle Name')
    last_name = models.CharField(max_length=80, verbose_name='Last Name')
    gender  = models.CharField(max_length=80, verbose_name='Gender', choices=GENDER)
    date_of_birth = models.DateField(verbose_name='Date of Birth', blank=False, null=False)
    ministry_or_angency = models.ForeignKey(MinistryAgency, on_delete=models.CASCADE)
    date_hire  = models.DateField(verbose_name='Date Hire', blank=False, null=False)
    department_name = models.ForeignKey(Department, on_delete= models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='employee_pics')
    address = models.CharField(verbose_name='Address', max_length=100)
    city = models.CharField(verbose_name='City', max_length=100)
    county = models.CharField(max_length=4, choices=COUNTY)
    email = models.EmailField()
    mobile = models.CharField(max_length=15, blank=True, null=True)
    recorded_on = models.DateTimeField(auto_now=True, auto_now_add=False)



    def __str__(self):
        return self.employee_ref

    class Meta:
        db_table = 'hr_employee'
        managed = True
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

class JobHistory(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField('Start Date', blank=True, null=True)
    end_date = models.DateField('End Date', blank=True, null=True)

    def __str_(self):
        return self.employee

    class Meta:
        db_table = 'hr_jobhistory'
        verbose_name_plural = 'Job Histories'
        verbose_name = 'Job History'

class Dependant(models.Model):
    

    def __str__(self):
        pass

    class Meta:
        db_table = 'hr_address'
        managed = True
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

CONTRACT_TYPE = (
    ('Full-Time', 'FTIM'),
    ('Part-Time', 'PTIM'),
    ('Fixed-Term', 'FTER'),
    ('Agency Staff', 'AGEN'),
    ('Freelancer','FREE'),
    ('Consultant', 'CSUL'),
    ('Controctor', 'COTR'),
    ('Volunteer', 'VOLU'),

)
class Contract(models.Model):
    contract_reference = models.CharField(max_length=15, default=get_uniqueId)
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE)
    contract_type = models.CharField(max_length=10, choices=CONTRACT_TYPE)
    contract_title = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField('Start Date')
    expire_date = models.DateField('Expire Date', blank=True,null=True)
    gross_base_salary = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, default='Active')
    note = models.TextField(blank=True,null=True)


    def __str_(self):
        return contract_reference

    class Meta:
        db_table = 'hr_contract'
        unique_together = ('contract_reference', 'employee')