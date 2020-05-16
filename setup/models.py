from django.db import models
from django.urls import reverse
from phone_field import PhoneField
from datetime import date, datetime
from decimal import Decimal
from django.db.models import Sum


class ReportType(models.Model):
    abbreviation = models.CharField(max_length=4, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.description + "(" + self.abbreviation + ")"


class Agent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    home_phone = PhoneField(blank=True, help_text='Home phone number')
    mobile_phone = PhoneField(blank=True, help_text='Mobile phone number')
    notes = models.CharField(max_length=250, blank=True, null=True)
    rate_ime = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    rate_ad = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    rate_pr = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    rate_ns = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    rate_ex = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    rate_ar = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.first_name+" "+self.last_name

    def get_absolute_url(self):
        return reverse('agents-detail', kwargs={'pk': self.pk})


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    home_phone = PhoneField(blank=True, help_text='Home phone number')
    mobile_phone = PhoneField(blank=True, help_text='Mobile phone number')
    cmpa = models.IntegerField(blank=True, null=True)
    cpso = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=250, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    rate_ime = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    rate_ad = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    rate_pr = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    rate_ns = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    rate_ex = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    rate_ar = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('doctors-detail', kwargs={'pk': self.pk})


class Source(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    office_phone = PhoneField(blank=True, help_text='Office phone number')
    main_contact = models.CharField(max_length=150, blank=True, null=True)
    contact_email = models.EmailField(max_length=254, blank=True, null=True)
    contact_phone = PhoneField(blank=True, help_text='Main Contact phone number')
    billing_contact = models.CharField(max_length=150, blank=True, null=True)
    billing_email = models.EmailField(max_length=254, blank=True, null=True)
    billing_phone = PhoneField(blank=True, help_text='Billing Contact phone number')
    notes = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('sources-detail', kwargs={'pk': self.pk})


class Rate(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.source.name + " " + self.report_type.description + " " + str(self.amount)

    def get_absolute_url(self):
        return reverse('rates-detail', kwargs={'pk': self.pk})


class Clinic(models.Model):
    name = models.CharField(max_length=150, verbose_name="Clinic Name")
    address = models.CharField(max_length=150)
    main_contact = models.CharField(max_length=150, blank=True, null=True)
    office_phone = PhoneField(blank=True, help_text='Office phone number')
    email = models.EmailField(max_length=254, blank=True, null=True)
    notes = models.CharField(max_length=250, blank=True, null=True)
    rate_ime = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    rate_ns = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('clinics-detail', kwargs={'pk': self.pk})


class Claimant(models.Model):    
    source = models.ForeignKey(Source, on_delete = models.CASCADE)
    GENDER_CHOICES = [('Mr', 'Mr'),('Mrs', 'Mrs'),('Miss', 'Miss'),]
    title = models.CharField(max_length=4, choices=GENDER_CHOICES)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()  
    claim_number = models.CharField(max_length=20, null=True, blank=True)
    date_of_accident = models.DateField(blank=True, null=True)
    
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()

    def save(self, *args, **kwargs):
        import datetime                
        self.age = int((datetime.date.today() - self.date_of_birth).days / 365.25)
        self.full_name = self.title + ' ' + self.first_name + ' ' + self.last_name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name
    
    def get_absolute_url(self):
        return reverse('claimants-detail', kwargs={'pk': self.pk})

    
class Assessment(models.Model):
    claimant = models.ForeignKey(Claimant, on_delete = models.CASCADE)    
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.claimant.full_name
    
    def get_absolute_url(self):
        return reverse('assessments-detail', kwargs={'pk': self.pk})


class Invoice(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete = models.CASCADE)
    report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE, null=True, blank=True)
    number = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    tax = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    applied = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=0)    
    balance = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):        
        self.balance = self.total - self.applied
        super().save(*args, **kwargs)
        
    def __str__(self):
        return str(self.number)
    
    def get_absolute_url(self):
        return reverse('invoices-detail', kwargs={'pk': self.pk})


class SourcePayment(models.Model):
    source = models.ForeignKey(Source, on_delete = models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    date = models.DateField(null=True, blank=True)
    reference_number = models.CharField(max_length=20, null=True, blank=True)
    tax = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    applied = models.BooleanField(default=False)
    abbreviation = models.CharField(max_length=2, default='CR', blank=True, null=True)

    def save(self, *args, **kwargs):
        ratio = 0.13/1.13      
        self.tax = round(float(self.amount) * ratio,2)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.source.name + " " + self.reference_number
    
    def get_absolute_url(self):
        return reverse('sourcepayments-list')


class ApplyPayment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete = models.CASCADE)
    sourcepayment = models.ForeignKey(SourcePayment, on_delete = models.CASCADE)
    date = models.DateField(null=True, blank=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):        
        self.date = date.today()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.invoice) + " " + str(self.sourcepayment.reference_number)
    
    def get_absolute_url(self):
        return reverse('applypayments-detail', kwargs={'pk': self.pk})


class Expense(models.Model):    
    EXPENSE_TYPE = [
        ('Physician payout', 'Physician payout'),
        ('Agent payout', 'Agent payout'),
        ('Clinic rent', 'Clinic rent'),
        ('Other expense', 'Other expense'),
        ('Consulting fees', 'Consulting fees'),
    ]

    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True, null=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, blank=True, null=True)
    reference = models.CharField(max_length=15, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=100, choices=EXPENSE_TYPE)
    payee = models.CharField(max_length=100, null=True, blank=True)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    tax = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    note = models.CharField(max_length=200, null=True, blank=True, default = 'Expense')
    abbreviation = models.CharField(max_length=2, null=True, blank=True, default='DR')
    
    def save(self, *args, **kwargs):
        self.date = date.today()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.payee 
    
    def get_absolute_url(self):
        return reverse('expenses-detail', kwargs={'pk': self.pk})


class DoctorBill(models.Model):
    invoice = models.OneToOneField(Invoice, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True, null=True)
    expense = models.ForeignKey(Expense, on_delete=models.SET_NULL, null=True, blank=True)
    bill_date = models.DateField(null=True, blank=True)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default = 0.00)
    tax = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default = 0.00)
    total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    paid = models.BooleanField(default=False)
    paid_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.tax = self.subtotal * Decimal(0.13)
        self.total = self.subtotal * Decimal(1.13)
        self.bill_date = date.today()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.invoice)
    
    def get_absolute_url(self):
        return reverse('doctorbills-detail', kwargs={'pk': self.pk})


class AgentBill(models.Model):
    invoice = models.OneToOneField(Invoice, on_delete = models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, blank=True, null=True)
    expense = models.ForeignKey(Expense, on_delete=models.SET_NULL, null=True, blank=True)
    bill_date = models.DateField(null=True, blank=True)    
    total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    paid = models.BooleanField(default=False)
    paid_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.bill_date = date.today()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.invoice)
    
    def get_absolute_url(self):
        return reverse('agentbills-detail', kwargs={'pk': self.pk})


class ClinicBill(models.Model):
    invoice = models.OneToOneField(Invoice, on_delete = models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, blank=True, null=True)
    expense = models.ForeignKey(Expense, on_delete=models.SET_NULL, null=True, blank=True)
    bill_date = models.DateField(null=True, blank=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    paid = models.BooleanField(default=False)
    paid_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.bill_date = date.today()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.invoice)
    
    def get_absolute_url(self):
        return reverse('clinicbills-detail', kwargs={'pk': self.pk})



    
