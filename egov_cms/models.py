from django.db import models
from egov_hr.models import Employee

GENDER = (('F', 'Female'),('M', 'Male'),)
TITLE = (('Mr','Mr'),('Miss','Miss'),)
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

""" class Agency(models.Model):
    agency_code = models.CharField(max_length=6)
    agency_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.agency_code
class Department(models.Model):
    department_code = models.CharField(max_length=10)
    department_name = models.CharField(max_length=170)

    def __str__(self):
        return self.department_code """

""" class Employee(models.Model):
    employee_id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=5, choices=TITLE)
    first_name = models.CharField('First Name', max_length=100)
    middle_name = models.CharField('Middle Name', max_length=100)
    last_name = models.CharField('Last Name', max_length=100)
    gender = models.CharField(max_length=2, choices=GENDER)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=170)
    date_hired = models.DateField(auto_now=False, auto_now_add=True)
    date_of_birth = models.DateField('Date of Birth', auto_now=False, auto_now_add=True)
    telephone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    photo = models.ImageField(upload_to=None, default='')
    status = models.CharField(max_length=10, default='Active')
    note = models.TextField()
    
    def __str__(self):
        return self.employee_id """

class PrisonStaffRoles(models.Model):
    prison_staff_role_code = models.CharField(max_length=5, primary_key=True)
    role_code_description = models.CharField(max_length=150)

    def __str__(self):
        return self.prison_staff_role_code
class Cell(models.Model):
    cell_number = models.CharField(max_length=10)
    cell_description = models.CharField(max_length=200)

    def __str__(self):
        return self.cell_number
class Prison(models.Model):
    prison_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=150)
    prison_superintendent = models.CharField(max_length=200)
    address = models.CharField(max_length=70)
    county = models.CharField(max_length=5, choices=COUNTY)
    capacity = models.IntegerField('Prison Capacity',blank=True)
    telephone1 = models.CharField(max_length=15)
    telephone2 = models.CharField(max_length=15)
    email = models.EmailField()
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE)

    def __str__(self):
        return self.prison_id

class PrisonStaff(Employee):

    prison_role = models.ForeignKey(PrisonStaffRoles, on_delete=models.CASCADE)
    prison_assigned_to = models.ForeignKey(Prison, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_id

class Officer(Employee):
    officer_number = models.CharField(max_length=20)

    def __str__(self):
        return self.officer_number


class RelationshipType(models.Model):
    relationship_code = models.CharField(max_length=5)
    relationship_description = models.CharField(max_length=200)

    def __str__(self):
        return self.relationship_code

class NextOfKin(models.Model):
    first_name = models.CharField('First Name', max_length=100)
    middle_name = models.CharField('Middle Name', max_length=100)
    last_name = models.CharField('Last Name', max_length=100)
    gender = models.CharField(max_length=2, choices=GENDER)
    date_of_birth = models.DateField('Date of Birth', auto_now=False, auto_now_add=True)
    relationship_to_inmate = models.ForeignKey(RelationshipType, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.first_name + '' + self.last_name

class Solicitor(models.Model):
    solicitor_name = models.CharField(max_length=150)
    name_company = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=130, blank=True, null=True)
    telephone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.solicitor_name
class OffenceCategory(models.Model):
    offence_category_code = models.CharField(max_length=10, primary_key=True)
    offence_category_description = models.CharField(max_length=200)

    def __str__(self):
        return self.offence_category_code

class Offence(models.Model):
    offence_id = models.CharField(max_length=10, primary_key=True)
    offence_category = models.ForeignKey(OffenceCategory, on_delete=models.CASCADE)
    offence_short_name = models.CharField(max_length=50)
    offence_fullname = models.CharField(max_length=200, blank=True, null=True)
    offence_description = models.CharField(max_length=200, blank=True, null=True)
    min_sentence = models.CharField(max_length=10, blank=True, null=True)
    max_sentence = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.offence_id

class Inmate(models.Model):
    prisoner_id = models.CharField(max_length=20, primary_key=True)
    prison_id = models.ForeignKey(Prison, on_delete=models.CASCADE)
    first_name = models.CharField('First Name', max_length=100)
    middle_name = models.CharField('Middle Name', max_length=100)
    last_name = models.CharField('Last Name', max_length=100)
    gender = models.CharField(max_length=2, choices=GENDER)
    date_of_birth = models.DateField('Date of Birth', auto_now=False, auto_now_add=True)
    place_of_birth = models.CharField('Place of Birth', max_length= 150)
    next_of_kin = models.ManyToManyField(NextOfKin, through='InmateFamily')
    inmate_address = models.CharField(max_length=150, blank=True, null=True)
    offence = models.ManyToManyField(Offence)
    probation_hearing_due_date = models.DateField(auto_now=False, auto_now_add=True, blank=True, null=True)
    solicitor_name = models.ForeignKey(Solicitor, on_delete=models.CASCADE)
    inmate_photo = models.ImageField(upload_to=None)
    note = models.TextField()
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.prisoner_id

class MedicalInformation(models.Model):
    prisoner_id = models.ForeignKey(Inmate, on_delete=models.CASCADE)
    disablity = models.BooleanField(default=False)

    def __str__(self):
        return self.prisoner_id


class InmateFamily(models.Model):
    prisoner_id = models.ForeignKey(Inmate, on_delete=models.CASCADE)
    Next_of_kin = models.ForeignKey(NextOfKin, on_delete=models.CASCADE)

    def __str__(self):
        return self.prisoner_id
class ComplainCategory(models.Model):
    complain_category_code = models.CharField(max_length=10)
    category_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.complain_category_code

class InformationSource(models.Model):
    information_source_code = models.CharField(max_length=5)
    information_source_name = models.CharField(max_length=130)
    information_source_description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.information_source_code

class Complain(models.Model):
    complain_log_number = models.CharField(max_length=20)
    information_source = models.ForeignKey(InformationSource, on_delete=models.CASCADE)
    full_name_complainant = models.CharField(max_length=200, blank=True, null=True)
    nature_of_complain = models.ForeignKey(ComplainCategory, on_delete=models.CASCADE)
    complainant_statement = models.TextField(blank=True, null=True)
    defendant_statement = models.TextField(blank=True, null=True)
    current_date_time = models.DateTimeField(auto_now=True,auto_now_add=False)
    date_of_incidence = models.DateField(auto_now=False, auto_now_add=True)
    officer_on_case = models.ForeignKey(Officer,on_delete=models.CASCADE)
    arrest_made = models.BooleanField()
    number_of_arrest_made = models.IntegerField(default=0)


    note = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.complain_log_number




class IncidenceType(models.Model):
    incidence_type_code = models.CharField(max_length=10)
    incidence_type_description = models.CharField(max_length=200)

    def __str__(self):
        return self.incidence_type_code

class Incidence(models.Model):
    incidence_id = models.CharField(max_length=30, primary_key=True)
    date_of_incidence = models.DateField(auto_now=False, auto_now_add=True)
    type_of_incidence = models.ForeignKey(IncidenceType, on_delete=models.CASCADE)
    information_source = models.CharField(max_length=200)
    time_recorded = models.DateTimeField( auto_now=True, auto_now_add=False)
    incidence_location = models.CharField(max_length=200, blank=True, null=True)
    name_of_person_reporting = models.CharField(max_length=150, blank=True, null=True)
    reporter_telephone_number = models.CharField(max_length=20, blank=True, null=True)
    officer_incharged = models.ForeignKey(Officer, on_delete=models.CASCADE)
    note = models.CharField(max_length=254, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.incidence_id

class PoliceStation(models.Model):
    station_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    electoral_zone = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.station_id

