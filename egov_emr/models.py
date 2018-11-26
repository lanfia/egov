from django.db import models
import uuid
import datetime



TITLE = (
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Miss', 'Miss'),
    ('Sir', 'Sir'),
    ('Dr', 'Dr'),
)
GENDER = (
    ('F', 'Female'),
    ('M', 'Male'), ('N', 'Not Disclosed'),

)


class Country(models.Model):
    country_code = models.CharField(max_length=5,)
    country_name = models.CharField(max_length=180)

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class HealthCenter(models.Model):

    HEALTH_CENTER_CATEGORY = (
        ('CLN', 'Clinic'),
        ('HOP', 'Hopital'),
        ('RHP', 'Referer Hospital'),
        ('DNS', 'Dental Surgery'),
    )

    health_center_name = models.CharField(max_length=150,)
    address = models.CharField(max_length=200,)
    street = models.CharField(max_length=200,)
    city = models.CharField(max_length=200,)
    county_provence = models.CharField(max_length=200,)
    country = models.ForeignKey(
        'Country',  on_delete=models.CASCADE)
    telephone_number = models.IntegerField()
    email = models.EmailField()
    category = models.CharField(max_length=200, choices=HEALTH_CENTER_CATEGORY)

    def __str__(self):
        return self.health_center_name


class Allergy(models.Model):
    ALLEGY_CATEGORY = (
        ('Drug', 'Drug'),
        ('Food', 'Food'),
        ('Other', 'Other'),
    )

    allegy = models.CharField(max_length=40)
    allegy_category = models.CharField(max_length=5, choices=ALLEGY_CATEGORY)

    def __str__(self):
        return self.allegy


class Reaction(models.Model):
    reaction = models.CharField(max_length=50)

    def __str__(self):
        return self.reaction


class NextOfKin(models.Model):
    RELATIONSHIP = (
        ('Mother', 'Moth'),
        ('Father', 'Fath'),
        ('Brother', 'Brot'),
        ('Spouse', 'Spou'),
        ('Uncle', 'Uncl'),


    )
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    middle_name = models.CharField(
        max_length=100, verbose_name='Middle Name', blank=True, null=True)
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    occupation = models.CharField(
        max_length=100, verbose_name='Occupation', blank=True, null=True)
    relationship_to_patience = models.CharField(
        max_length=40, verbose_name='Relationship', choices=RELATIONSHIP)
    mobile_number = models.CharField(
        max_length=15, verbose_name='Mobile Phone Number', blank=True, null=True)
    email = models.EmailField(verbose_name='Email Address')
    address = models.TextField()

    def __str__(self):
        return self.first_name + '' + self.last_name


class PatienceRecord(models.Model):

    def get_uniqueId():
        current_month = str(datetime.date.today().month)
        current_year = str(datetime.date.today().year)

        return str(uuid.uuid4())[:8].upper() + '-' + current_month + current_year

    patience_ref = models.CharField(
        max_length=10, primary_key=True, default=get_uniqueId,)
    #account = models.OneToOneField(Account, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=5, choices=TITLE, blank=True, null=True, verbose_name='Title')
    patience_first_name = models.CharField(
        max_length=110, verbose_name='First Name')
    patience_middle_name = models.CharField(
        max_length=110, blank=True, null=True, verbose_name='Middle Name')
    patience_last_name = models.CharField(
        max_length=110, verbose_name='Last Name')

    date_of_birth = models.DateField(
        auto_now=False, auto_now_add=True, verbose_name='Date of Birth')
    nationality = models.ForeignKey(Country, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER)
    telephone_number = models.CharField(max_length=13, blank=True, null=True)
    mobile_number = models.CharField(max_length=13, blank=True, null=True)
    health_center_registered_to = models.ForeignKey(
        HealthCenter, on_delete=models.CASCADE)
    next_of_kin = models.ManyToManyField(NextOfKin, verbose_name='Next of Kin')

    def create_patient_account(sender, instance, created, **kwargs):
        if created:
            Account.objects.create(account=instance)
        instance.account.save()

    def fullName(self):
        full_name = self.patience_first_name + '' + \
            self.patience_middle_name + '' + self.patience_last_name
        return full_name

    def __str__(self):
        return str(self.patience_ref)


class PatienceAllegy(models.Model):
    SEVERITY_CAT = (
        ('Mild', 'MID'),
        ('Moderate', 'MOD'),
        ('Severe', 'SEV'),
    )
    patience_record = models.ForeignKey(
        PatienceRecord, on_delete=models.CASCADE)
    allegy = models.ManyToManyField(Allergy)
    severity = models.CharField(max_length=10, choices=SEVERITY_CAT)

    def __str__(self):
        return self.allegy


class DiagnosticCategory(models.Model):
    cat_code = models.CharField(max_length=10)
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Diagnostic Category"
        verbose_name_plural = "Diagnostic Categories"


class Diagnostic(models.Model):
    test_code = models.CharField(max_length=10)
    diagnostic_category = models.ForeignKey(
        DiagnosticCategory, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=120)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.test_name

    class Meta:
        verbose_name = "Diagnostic"
        verbose_name_plural = "Diagnostics"


class Visit(models.Model):
    patience_record = models.ForeignKey(
        PatienceRecord, on_delete=models.CASCADE)
    visit_date = models.DateField('Vist Date')
    created_on = models.DateField(auto_now=False, auto_now_add=True)
    reason_for_visit = models.TextField(blank=True, null=True)
    diagnostics_required = models.ManyToManyField(Diagnostic)
    status = models.CharField(max_length=20, default='active')
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.patience_record

    class Meta:
        ordering = ('patience_record',)


class Vital(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    height = models.DecimalField(
        max_digits=2, decimal_places=1, verbose_name="Height(cm)")
    weight = models.DecimalField(
        max_digits=2, decimal_places=1, verbose_name="Weight(kg)")
    temperature = models.DecimalField(max_digits=2, decimal_places=1,)
    pulse = models.IntegerField()
    respiratory_rate = models.DecimalField(max_digits=2, decimal_places=1,)
    blood_pressure_r1 = models.DecimalField(max_digits=2, decimal_places=1,)
    blood_pressure_r2 = models.DecimalField(max_digits=2, decimal_places=1,)
    blood_oxygen_saturation = models.DecimalField(
        max_digits=2, decimal_places=1,)
    recorded_on = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        pass


class DiagnosticResult(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='active')
    note = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Diagnostic Result"
        verbose_name_plural = "Diagnostic Results"

    def __str__(self):
        return self.visit