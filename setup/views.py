from django.shortcuts import render, redirect, get_object_or_404
from .models import Assessment, Doctor, Clinic, Agent, Source, Rate, Payment, ApplyPayment, DoctorBill, AgentBill, ClinicBill, Claimant
from .forms import AgentForm, DoctorForm, ClinicForm, SourceForm, AssessmentForm, InvoiceForm, RateForm, PaymentForm, ApplyPaymentForm, ClaimantForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from datetime import date
from django.contrib import messages
from django.db.models import Sum




def Index(request):
    return render(request, 'setup/index.html')


def About(request):
    return render(request, 'setup/about.html')


def Contact(request):
    return render(request, 'setup/contact.html')

# -----------------------Agent Views---------------------------------------


class AgentListView(ListView):
    model = Agent
    form_class = AgentForm
    template_name = 'setup/agent_list.html'
    context_object_name = 'agents'


class AgentDetailView(DetailView):
    model = Agent
    template_name = 'setup/agent_detail.html'
    context_object_name = 'agent'


class AgentCreateView(CreateView):
    model = Agent
    template_name = 'setup/agent_form.html'
    form_class = AgentForm
    #initial = {"Email": "Ijaz Email"}
    

class AgentUpdateView(UpdateView):
    model = Agent
    template_name = 'setup/agent_form.html'
    form_class = AgentForm
    

class AgentDeleteView(DeleteView):
    model = Agent
    template_name = 'setup/agent_confirm_delete.html'
    context_object_name = 'agent'
    success_url = '/agents/'
    

# -----------------------Doctor Views---------------------------------------


class DoctorListView(ListView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'setup/doctor_list.html'
    context_object_name = 'doctors'


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'setup/doctor_detail.html'
    context_object_name = 'doctor'


class DoctorCreateView(CreateView):
    model = Doctor
    template_name = 'setup/doctor_form.html'
    form_class = DoctorForm
    

class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    # will use doctor_form.html template as default


class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'setup/doctor_confirm_delete.html'
    success_url = '/doctors/'
    context_object_name = 'doctor'

# -----------------------Clinic Views---------------------------------------


class ClinicListView(ListView):
    model = Clinic
    form_class = ClinicForm
    template_name = 'setup/clinic_list.html'
    context_object_name = 'clinics'


class ClinicDetailView(DetailView):
    model = Clinic
    template_name = 'setup/clinic_detail.html'
    context_object_name = 'clinic'


class ClinicCreateView(CreateView):
    model = Clinic
    template_name = 'setup/clinic_form.html'
    form_class = ClinicForm
    

class ClinicUpdateView(UpdateView):
    model = Clinic
    template_name = 'setup/clinic_form.html'
    form_class = ClinicForm
    

class ClinicDeleteView(DeleteView):
    model = Clinic
    template_name = 'setup/clinic_confirm_delete.html'
    success_url = '/clinics/'
    context_object_name = 'clinic'
    

# -----------------------Source Views---------------------------------------

class SourceListView(ListView):
    model = Source
    form_class = SourceForm
    template_name = 'setup/source_list.html'
    context_object_name = 'sources'


class SourceDetailView(DetailView):
    model = Source
    template_name = 'setup/source_detail.html'
    context_object_name = 'source'

    def get_context_data(self, *args, **kwargs):
        context = super(SourceDetailView, self).get_context_data(*args, **kwargs)
        #context['rates'] = self.object.rate_set.all().order_by('-Amount')  **THis also does the same thing
        context['rates'] = Rate.objects.all().filter(Source=self.object).order_by('-Amount')
        #context['rates'] = Rate.objects.all().filter(Source=self.kwargs['pk']).order_by('-Amount')    **This also does the same thing
        return context


class SourceCreateView(CreateView):
    model = Source
    template_name = 'setup/source_form.html'
    form_class = SourceForm
    

class SourceUpdateView(UpdateView):
    model = Source
    template_name = 'setup/source_form.html'
    form_class = SourceForm
    

class SourceDeleteView(DeleteView):
    model = Source
    template_name = 'setup/source_confirm_delete.html'
    success_url = '/sources/'
    context_object_name = 'source'


# -----------------------Claimant Views---------------------------------------


class ClaimantListView(ListView):
    model = Claimant
    form_class = ClaimantForm
    template_name = 'setup/claimant_list.html'
    context_object_name = 'claimants'


class ClaimantDetailView(DetailView):
    model = Claimant
    template_name = 'setup/claimant_detail.html'
    context_object_name = 'claimant'


class ClaimantCreateView(CreateView):
    model = Claimant
    template_name = 'setup/claimant_form.html'
    form_class = ClaimantForm  
    

class ClaimantUpdateView(UpdateView):
    model = Claimant
    template_name = 'setup/claimant_form.html'
    form_class = ClaimantForm
    

class ClaimantDeleteView(DeleteView):
    model = Claimant
    template_name = 'setup/claimant_confirm_delete.html'
    context_object_name = 'claimant'
    success_url = '/claimants/'

# -----------------------Assessment Views---------------------------------------

class AssessmentListView(ListView):
    model = Assessment
    form_class = AssessmentForm
    template_name = 'setup/assessment_list.html'
    context_object_name = 'assessments'

    
class AssessmentDetailView(DetailView):
    model = Assessment
    template_name = 'setup/assessment_detail.html'
    context_object_name = 'assessment'

    def get_context_data(self, *args, **kwargs):
        context = super(AssessmentDetailView, self).get_context_data(*args, **kwargs)
        #context['rates'] = self.object.rate_set.all().order_by('-Amount')  **THis also does the same thing
        #context['invoices'] = Invoice.objects.all().filter(Assessment=self.object).order_by('-Date')
        context['payments'] = ApplyPayment.objects.filter(assessment=self.kwargs['pk'])   
        return context

    
class AssessmentCreateView(CreateView):
    model = Assessment
    template_name = 'setup/assessment_form.html'
    form_class = AssessmentForm     
    

class AssessmentUpdateView(UpdateView):
    model = Assessment
    template_name = 'setup/assessment_form.html'
    form_class = AssessmentForm
    

class AssessmentDeleteView(DeleteView):
    model = Assessment
    template_name = 'setup/assessment_confirm_delete.html'
    success_url = '/assessments/'
    context_object_name = 'assessment'

# -----------------------Invoice Views---------------------------------------

class InvoiceListView(ListView):
    model = Assessment
    form_class = InvoiceForm
    template_name = 'setup/invoice_list.html'
    context_object_name = 'invoices'

    def get_queryset(self):
        try:
            search = self.request.GET.get('search',)
        except KeyError:
            search = None
        if search:
            invoices = Assessment.objects.filter(InvoiceNumber=search)
        else:
            invoices = Assessment.objects.all()
        return invoices


class InvoiceDetailView(DetailView):
    model = Assessment
    template_name = 'setup/invoice_detail.html'    
    context_object_name = 'invoice'


class InvoiceCreateView(UpdateView):
    model = Assessment
    template_name = 'setup/invoice_form.html'
    form_class = InvoiceForm
    # initial = {"InvoiceSubtotal": '500'}
    
    def get_context_data(self, *args, **kwargs):
        context = super(InvoiceCreateView, self).get_context_data(**kwargs) 
        source_pk = self.kwargs['source_pk']
        report_pk = self.kwargs['report_pk']               
        context['hold'] = Rate.objects.get(Source=source_pk, Report_Type=report_pk)
        return context    
            

class InvoiceUpdateView(UpdateView):
    model = Assessment
    template_name = 'setup/invoice_form.html'
    form_class = InvoiceForm

# -----------------------Rate Views---------------------------------------
    

class RateListView(ListView):
    model = Rate
    form_class = RateForm
    template_name = 'setup/rate_list.html'
    context_object_name = 'rates'


class RateDetailView(DetailView):
    model = Rate
    template_name = 'setup/rate_detail.html'
    context_object_name = 'rate'


class RateCreateView(CreateView):
    model = Rate
    template_name = 'setup/rate_form.html'
    form_class = RateForm
    #initial = {"Email": "Ijaz Email"}
    

class RateUpdateView(UpdateView):
    model = Rate
    template_name = 'setup/rate_form.html'
    form_class = RateForm
    

class RateDeleteView(DeleteView):
    model = Rate
    template_name = 'setup/rate_confirm_delete.html'
    context_object_name = 'rate'
    success_url = '/rates/'
    

# -----------------------Payment Views---------------------------------------
    

class PaymentListView(ListView):
    model = Payment
    form_class = PaymentForm    
    template_name = 'setup/payment_list.html'
    context_object_name = 'payment'


class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'setup/payment_detail.html'
    context_object_name = 'payment'


class PaymentCreateView(CreateView):
    model = Payment
    template_name = 'setup/payment_form.html'
    form_class = PaymentForm
    #initial = {"Email": "Ijaz Email"}
    

class PaymentUpdateView(UpdateView):
    model = Payment
    template_name = 'setup/payment_form.html'
    form_class = PaymentForm
    

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'setup/payment_confirm_delete.html'
    context_object_name = 'payment'
    success_url = '/payments/'
    

# -----------------------ApplyPayment Views---------------------------------------
    

class ApplyPaymentListView(ListView):
    model = ApplyPayment
    form_class = ApplyPaymentForm    
    template_name = 'setup/applypayment_list.html'
    context_object_name = 'applypayment'


class ApplyPaymentDetailView(DetailView):
    model = ApplyPayment
    template_name = 'setup/applypayment_detail.html'
    context_object_name = 'applypayment'


class ApplyPaymentCreateView(CreateView):
    model = ApplyPayment
    template_name = 'setup/applypayment_form.html'
    form_class = ApplyPaymentForm
    #initial = {"Email": "Ijaz Email"}
    

class ApplyPaymentUpdateView(UpdateView):
    model = ApplyPayment
    template_name = 'setup/applypayment_form.html'
    form_class = ApplyPaymentForm
    

class ApplyPaymentDeleteView(DeleteView):
    model = ApplyPayment
    template_name = 'setup/applypayment_confirm_delete.html'
    context_object_name = 'applypayment'
    success_url = '/applypayments/'


def CreateDoctorInvoice(assessment_id):
    assessment = Assessment.objects.get(id=assessment_id)
    abr = assessment.Report_Type.Abbreviation
    if abr == 'IME':
        bill = assessment.Doctor.Rate_IME
    elif abr == 'AD':
        bill = assessment.Doctor.Rate_AD
    elif abr == 'PR':
        bill = assessment.Doctor.Rate_PR
    elif abr == 'NS':
        bill = assessment.Doctor.Rate_NS
    elif abr == 'EX':
        bill = assessment.Doctor.Rate_EX
        
    doctorbill = DoctorBill(assessment=assessment, BillSubtotal=bill)
    doctorbill.save()
    return


def CreateAgentInvoice(assessment_id):
    assessment = Assessment.objects.get(id=assessment_id)
    abr = assessment.Report_Type.Abbreviation
    if abr == 'IME':
        bill = assessment.Agent.Rate_IME
    elif abr == 'AD':
        bill = assessment.Agent.Rate_AD
    elif abr == 'PR':
        bill = assessment.Agent.Rate_PR
    elif abr == 'NS':
        bill = assessment.Agent.Rate_NS
    elif abr == 'EX':
        bill = assessment.Agent.Rate_EX
        
    agentbill = AgentBill(assessment=assessment, BillTotal=bill)
    agentbill.save()
    return


def CreateClinicInvoice(assessment_id):
    assessment = Assessment.objects.get(id=assessment_id)
    abr = assessment.Report_Type.Abbreviation
    if abr == 'IME':
        bill = assessment.Clinic.Rate_IME
    elif abr == 'NS':
        bill = assessment.Clinic.Rate_NS
    else:
        return

    clinicbill = ClinicBill(assessment=assessment, BillTotal=bill)
    clinicbill.save()
    return


def InvoicePaidSwitch(invoice_id):
    invoice = Assessment.objects.get(id=invoice_id)
    invoice_total = invoice.InvoiceTotal    
    applied_invoices = ApplyPayment.objects.filter(assessment=invoice_id)    
    applied_total = applied_invoices.aggregate(Sum('Amount'))["Amount__sum"]
       
    if invoice_total == applied_total:
        invoice.InvoicePaid = True
        CreateDoctorInvoice(invoice_id)
        CreateAgentInvoice(invoice_id)
        CreateClinicInvoice(invoice_id)
    else:
        invoice.InvoicePaid = False
    invoice.save()    
    return  
    

# def ProcessPayment(request, pk): #pk is the Source Payment cheque id
#     #initialize search string to a blank, as there is no search at the start and this is being passed in the context    
#     invoice_search = ""
#     #get source payment object to process invoice payments         
#     payment = Payment.objects.get(id=pk)
#     #find all applied payments related to this Source Payment
#     applied = ApplyPayment.objects.filter(payment=pk)
#     #initial default data string setup         
#     initialdata = {'payment': pk, 'Date': date.today()}
#     #running balance of all invoices already applied to this Source Payment. returns dictionary!    
#     total_applied = applied.aggregate(Sum('Amount'))    
    
#     if 'search' in request.GET:
#         search = request.GET['search'] 
#         #find all invoices in Assessments with invoice#=search AND Source company with above Payment pk       
#         invoice_search = Assessment.objects.get(InvoiceNumber=search, Source=payment.Source)
                
#         if invoice_search is not None:

#             if ApplyPayment.objects.filter(assessment=invoice_search):
#                 if invoice_search.InvoicePaid == True:
#                     messages.error(request, 'Invoice Already applied')
#                     return redirect('process', pk)

#             newdata = {'assessment': invoice_search.id}
#             initialdata.update(newdata)
#         else:
#             messages.error(request, 'Invoice Not Found')
#             return redirect('process', pk) 

#     if request.method == 'POST':
#         # Create a form instance and populate it with data from the request (binding):
#         form = ApplyPaymentForm(request.POST, initial=initialdata)
#         # Check if the form is valid:
#         if form.is_valid():
#             applypayment_assessment = form.cleaned_data['assessment']
#             x = form.cleaned_data['Amount']            
#             z = Assessment.objects.get(id=applypayment_assessment.id).InvoiceTotal          

#             if x > z:
#                 messages.error(request, 'Applied amount cannot be higher than invoice amount')
#                 return redirect('process', pk)
            
#             form.save()                        
#             InvoicePaidSwitch(applypayment_assessment.id)            
#             return redirect('process', pk)           

#     # If this is a GET (or any other method) create the default form.
#     else:
#         form = ApplyPaymentForm(initial=initialdata)

#     context = {
#         'form': form,
#         'payment': payment,
#         'invoice': invoice_search,
#         'applied': applied,
#         'total_applied': total_applied
#     }       
#     return render(request, 'setup/processpayment.html', context)

def ProcessPayment(request, pk):
    sourcepayment = Payment.objects.get(id=pk)
    applied = ApplyPayment.objects.filter(payment=pk)
    openinvoices = Assessment.objects.filter(Source=sourcepayment.Source, InvoicePaid = False)
    closedinvoices = Assessment.objects.filter(Source=sourcepayment.Source, InvoicePaid = True)
    total_applied = applied.aggregate(Sum('Amount'))
    balance = sourcepayment.Amount - total_applied["Amount__sum"]

    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = ApplyPaymentForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            applypayment_assessment = form.cleaned_data['assessment']
            x = form.cleaned_data['Amount']            
            z = Assessment.objects.get(id=applypayment_assessment.id).InvoiceTotal          

            if x > z:
                messages.error(request, 'Applied amount cannot be higher than invoice amount')
                return redirect('process', pk)
            
            form.save()                        
            InvoicePaidSwitch(applypayment_assessment.id)            
            return redirect('process', pk)           

    # If this is a GET (or any other method) create the default form.
    else:
        form = ApplyPaymentForm()


    context = {
        'form': form,
        'openinvoices': openinvoices,
        'closedinvoices': closedinvoices,
        'payment': sourcepayment,
        'total_applied': total_applied,
        'balance': balance,        
                
    }       
    return render(request, 'setup/processpayment.html', context)


    
