# Generated by Django 2.1.3 on 2018-11-21 08:00

from django.db import migrations, models
import django.db.models.deletion
import egov_emr.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allegy', models.CharField(max_length=40)),
                ('allegy_category', models.CharField(choices=[('Drug', 'Drug'), ('Food', 'Food'), ('Other', 'Other')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=5)),
                ('country_name', models.CharField(max_length=180)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Diagnostic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_code', models.CharField(max_length=10)),
                ('test_name', models.CharField(max_length=120)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Diagnostic',
                'verbose_name_plural': 'Diagnostics',
            },
        ),
        migrations.CreateModel(
            name='DiagnosticCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_code', models.CharField(max_length=10)),
                ('category_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Diagnostic Category',
                'verbose_name_plural': 'Diagnostic Categories',
            },
        ),
        migrations.CreateModel(
            name='DiagnosticResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='active', max_length=20)),
                ('note', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Diagnostic Result',
                'verbose_name_plural': 'Diagnostic Results',
            },
        ),
        migrations.CreateModel(
            name='HealthCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health_center_name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('county_provence', models.CharField(max_length=200)),
                ('telephone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('category', models.CharField(choices=[('CLN', 'Clinic'), ('HOP', 'Hopital'), ('RHP', 'Referer Hospital'), ('DNS', 'Dental Surgery')], max_length=200)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egov_emr.Country')),
            ],
        ),
        migrations.CreateModel(
            name='NextOfKin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Middle Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('occupation', models.CharField(blank=True, max_length=100, null=True, verbose_name='Occupation')),
                ('relationship_to_patience', models.CharField(choices=[('Mother', 'Moth'), ('Father', 'Fath'), ('Brother', 'Brot'), ('Spouse', 'Spou'), ('Uncle', 'Uncl')], max_length=40, verbose_name='Relationship')),
                ('mobile_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Mobile Phone Number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PatienceAllegy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('severity', models.CharField(choices=[('Mild', 'MID'), ('Moderate', 'MOD'), ('Severe', 'SEV')], max_length=10)),
                ('allegy', models.ManyToManyField(to='egov_emr.Allergy')),
            ],
        ),
        migrations.CreateModel(
            name='PatienceRecord',
            fields=[
                ('patience_ref', models.CharField(default=egov_emr.models.PatienceRecord.get_uniqueId, max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Sir', 'Sir'), ('Dr', 'Dr')], max_length=5, null=True, verbose_name='Title')),
                ('patience_first_name', models.CharField(max_length=110, verbose_name='First Name')),
                ('patience_middle_name', models.CharField(blank=True, max_length=110, null=True, verbose_name='Middle Name')),
                ('patience_last_name', models.CharField(max_length=110, verbose_name='Last Name')),
                ('date_of_birth', models.DateField(auto_now_add=True, verbose_name='Date of Birth')),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('N', 'Not Disclosed')], max_length=1)),
                ('telephone_number', models.CharField(blank=True, max_length=13, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=13, null=True)),
                ('health_center_registered_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egov_emr.HealthCenter')),
                ('nationality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egov_emr.Country')),
                ('next_of_kin', models.ManyToManyField(to='egov_emr.NextOfKin', verbose_name='Next of Kin')),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateField(verbose_name='Vist Date')),
                ('created_on', models.DateField(auto_now_add=True)),
                ('reason_for_visit', models.TextField(blank=True, null=True)),
                ('status', models.CharField(default='active', max_length=20)),
                ('note', models.TextField(blank=True, null=True)),
                ('diagnostics_required', models.ManyToManyField(to='egov_emr.Diagnostic')),
                ('patience_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egov_emr.PatienceRecord')),
            ],
            options={
                'ordering': ('patience_record',),
            },
        ),
        migrations.CreateModel(
            name='Vital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Height(cm)')),
                ('weight', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Weight(kg)')),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=2)),
                ('pulse', models.IntegerField()),
                ('respiratory_rate', models.DecimalField(decimal_places=1, max_digits=2)),
                ('blood_pressure_r1', models.DecimalField(decimal_places=1, max_digits=2)),
                ('blood_pressure_r2', models.DecimalField(decimal_places=1, max_digits=2)),
                ('blood_oxygen_saturation', models.DecimalField(decimal_places=1, max_digits=2)),
                ('recorded_on', models.DateField(auto_now=True)),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egov_emr.Visit')),
            ],
        ),
        migrations.AddField(
            model_name='patienceallegy',
            name='patience_record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egov_emr.PatienceRecord'),
        ),
        migrations.AddField(
            model_name='diagnosticresult',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egov_emr.Visit'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='diagnostic_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egov_emr.DiagnosticCategory'),
        ),
    ]
