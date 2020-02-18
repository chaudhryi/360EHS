from django.db import models
from django.urls import reverse
from phone_field import PhoneField
from datetime import date, datetime
from decimal import Decimal


class ReportType(models.Model):
    Abbreviation = models.CharField(max_length=4, blank=True, null=True)
    Description = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.Description + "(" + self.Abbreviation + ")"


class Agent(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254, blank=True, null=True)
    Address = models.CharField(max_length=200, blank=True, null=True)
    Hire_Date = models.DateField(blank=True, null=True)
    Home_Phone = PhoneField(blank=True, help_text='Home phone number')
    Mobile_Phone = PhoneField(blank=True, help_text='Mobile phone number')
    Notes = models.CharField(max_length=250, blank=True, null=True)
    Rate_IME = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Rate_AD = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Rate_PR = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Rate_NS = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Rate_EX = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.First_Name+" "+self.Last_Name

    def get_absolute_url(self):
        return reverse('agents-detail', kwargs={'pk': self.pk})


class Doctor(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254, blank=True, null=True)
    Address = models.CharField(max_length=200, blank=True, null=True)
    Home_Phone = PhoneField(blank=True, help_text='Home phone number')
    Mobile_Phone = PhoneField(blank=True, help_text='Mobile phone number')
    CMPA = models.IntegerField(blank=True, null=True)
    CPSO = models.IntegerField(blank=True, null=True)
    Notes = models.CharField(max_length=250, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    Rate_IME = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Rate_AD = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Rate_PR = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Rate_NS = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Rate_EX = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.First_Name+" "+self.Last_Name

    def get_absolute_url(self):
        return reverse('doctors-detail', kwargs={'pk': self.pk})


class Source(models.Model):
    Name = models.CharField(max_length=150)
    Address = models.CharField(max_length=150)
    Office_Phone = PhoneField(blank=True, help_text='Office phone number')
    Main_Contact = models.CharField(max_length=150, blank=True, null=True)
    Contact_Email = models.EmailField(max_length=254, blank=True, null=True)
    Contact_Phone = PhoneField(blank=True, help_text='Main Contact phone number')
    Billing_Contact = models.CharField(max_length=150, blank=True, null=True)
    Billing_Email = models.EmailField(max_length=254, blank=True, null=True)
    Billing_Phone = PhoneField(blank=True, help_text='Billing Contact phone number')
    Notes = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.Name
    
    def get_absolute_url(self):
        return reverse('sources-detail', kwargs={'pk': self.pk})


class Rate(models.Model):
    Source = models.ForeignKey(Source, on_delete=models.CASCADE)
    Report_Type = models.ForeignKey(ReportType, on_delete=models.CASCADE)
    Amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.Source.Name + " " + self.Report_Type.Description + " " + str(self.Amount)

    def get_absolute_url(self):
        return reverse('rates-detail', kwargs={'pk': self.pk})


class Clinic(models.Model):
    Name = models.CharField(max_length=150, verbose_name="Clinic Name")
    Address = models.CharField(max_length=150)
    Main_Contact = models.CharField(max_length=150, blank=True, null=True)
    Office_Phone = PhoneField(blank=True, help_text='Office phone number')
    Email = models.EmailField(max_length=254, blank=True, null=True)
    Notes = models.CharField(max_length=250, blank=True, null=True)
    Rate_IME = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Rate_NS = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.Name
    
    def get_absolute_url(self):
        return reverse('clinics-detail', kwargs={'pk': self.pk})


class Claimant(models.Model):    
    source = models.ForeignKey(Source, on_delete = models.CASCADE)
    GENDER_CHOICES = [('Mr', 'Mr'),('Mrs', 'Mrs'),('Miss', 'Miss'),]
    Title = models.CharField(max_length=4, choices=GENDER_CHOICES)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Date_Of_Birth = models.DateField()  
    Claim_Number = models.CharField(max_length=20, null=True, blank=True)
    Date_Of_Accident = models.DateField(blank=True, null=True)
    
    Full_Name = models.CharField(max_length=100)
    Age = models.IntegerField()

    def save(self, *args, **kwargs):
        import datetime                
        self.Age = int((datetime.date.today() - self.Date_Of_Birth).days / 365.25)
        self.Full_Name = self.Title + ' ' + self.First_Name + ' ' + self.Last_Name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Full_Name
    
    def get_absolute_url(self):
        return reverse('claimants-detail', kwargs={'pk': self.pk})



class Payment(models.Model):
    Source = models.ForeignKey(Source, on_delete = models.CASCADE, null=True, blank=True)
    Amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Date = models.DateField(null=True, blank=True)
    CheckNumber = models.CharField(max_length=20, null=True, blank=True)
    AppliedBalance = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Applied = models.BooleanField(default=False)

    def __str__(self):
        return self.Source.Name + " " + self.CheckNumber
    
    def get_absolute_url(self):
        return reverse('payments-detail', kwargs={'pk': self.pk})

    
class Assessment(models.Model):
    Source = models.ForeignKey(Source, on_delete = models.CASCADE)
    Report_Type = models.ForeignKey(ReportType, on_delete=models.CASCADE, null=True, blank=True)
    Clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Agent = models.ForeignKey(Agent, on_delete=models.CASCADE, blank=True, null=True)
    Claimant_Name = models.CharField(max_length=100)
    Claim_Number = models.CharField(max_length=20, null=True, blank=True)
    AssessmentDate = models.DateField(null=True, blank=True)
    AssessmentTime = models.TimeField(null=True, blank=True)
    InvoiceNumber = models.CharField(max_length=100, null=True, blank=True)
    InvoiceDate = models.DateField(null=True, blank=True)
    InvoiceSubtotal = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    InvoiceTax = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    InvoiceTotal = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)    
    InvoicePaid = models.BooleanField(default=False)

    def __str__(self):
        return self.Claimant_Name
    
    def get_absolute_url(self):
        return reverse('assessments-detail', kwargs={'pk': self.pk})


class ApplyPayment(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete = models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete = models.CASCADE)
    Date = models.DateField(null=True, blank=True)
    Amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):        
        self.Date = date.today()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.assessment.Claimant_Name + " " + self.payment.CheckNumber
    
    def get_absolute_url(self):
        return reverse('applypayments-detail', kwargs={'pk': self.pk})


class DoctorBill(models.Model):
    assessment = models.OneToOneField(Assessment, on_delete = models.CASCADE)
    BillDate = models.DateField(null=True, blank=True)
    BillSubtotal = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    BillTax = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    BillTotal = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    BillPaid = models.BooleanField(default=False)
    DatePaid = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.BillTax = self.BillSubtotal * Decimal(0.13)
        self.BillTotal = self.BillSubtotal * Decimal(1.13)
        self.BillDate = date.today()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.assessment


class AgentBill(models.Model):
    assessment = models.OneToOneField(Assessment, on_delete = models.CASCADE)
    BillDate = models.DateField(null=True, blank=True)    
    BillTotal = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    BillPaid = models.BooleanField(default=False)
    DatePaid = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.BillDate = date.today()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.assessment.Agent.Last_Name


class ClinicBill(models.Model):
    assessment = models.OneToOneField(Assessment, on_delete = models.CASCADE)
    BillDate = models.DateField(null=True, blank=True)
    BillTotal = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    BillPaid = models.BooleanField(default=False)
    DatePaid = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.BillDate = date.today()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.assessment.Clinic.Name
    
