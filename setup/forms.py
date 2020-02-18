from django import forms
from .models import Agent, Doctor, Clinic, Source, Assessment, Rate, Payment, ApplyPayment, Claimant


class DateInput(forms.DateInput):
    input_type = 'date'


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'
        widgets = {'Hire_Date': DateInput()}


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = '__all__'


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = '__all__'


class ClaimantForm(forms.ModelForm):
    class Meta:
        model = Claimant
        exclude = ['Age', 'Full_Name']
        widgets = {'Date_Of_Birth': DateInput(), 'Date_Of_Accident': DateInput()}


class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = '__all__'
        widgets = {'AssessmentDate': DateInput()}


class InvoiceForm(forms.ModelForm):
    class Meta: 
        model = Assessment
        fields = ('InvoiceNumber', 'InvoiceDate', 'InvoiceSubtotal', 'InvoiceTax', 'InvoiceTotal',) 
        widgets = {'InvoiceDate': DateInput()}


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = '__all__'


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        widgets = {'Date': DateInput()}


# class ApplyPaymentForm(forms.ModelForm):
#     class Meta:
#         model = ApplyPayment
#         fields = '__all__'
#         widgets = {'Date': DateInput()}
        
#     def __init__(self, *args, **kwargs): 
#         super(ApplyPaymentForm, self).__init__(*args, **kwargs)                       
#         self.fields['Date'].disabled = True
#         self.fields['assessment'].disabled = True
#         self.fields['payment'].disabled = True

class ApplyPaymentForm(forms.ModelForm):
    class Meta:
        model = ApplyPayment
        fields = ['Amount']        
        widgets = {'Amount': forms.TextInput(attrs={'size': 5})}
    