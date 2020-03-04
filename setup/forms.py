from django import forms
from .models import Agent, Doctor, Clinic, Source, Assessment, Rate, SourcePayment, ApplyPayment, Claimant, Invoice


class DateInput(forms.DateInput):
    input_type = 'date'


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'
        widgets = {'hire_date': DateInput()}


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
        exclude = ['age', 'full_name']
        widgets = {'date_of_birth': DateInput(), 'date_of_accident': DateInput()}


class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = '__all__'
        widgets = {'date': DateInput()}


class InvoiceForm(forms.ModelForm):
    class Meta: 
        model = Invoice
        fields = '__all__' 
        widgets = {'date': DateInput()}


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = '__all__'


class SourcePaymentForm(forms.ModelForm):
    class Meta:
        model = SourcePayment
        fields = '__all__'
        widgets = {'date': DateInput()}


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
        fields = ['amount']        
        widgets = {'amount': forms.TextInput(attrs={'size': 5})}
    