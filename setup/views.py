from django.shortcuts import render, redirect, get_object_or_404
from .models import Assessment, Doctor, Clinic, Agent, Source, Rate, SourcePayment, ApplyPayment, DoctorBill, AgentBill, ClinicBill, Claimant, Invoice, ReportType
from .forms import AgentForm, DoctorForm, ClinicForm, SourceForm, AssessmentForm, InvoiceForm, RateForm, SourcePaymentForm, ApplyPaymentForm, ClaimantForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from datetime import date
from django.contrib import messages
from django.db.models import Sum
from decimal import Decimal




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
    template_name = 'setup/agent/agent_list.html'
    context_object_name = 'agents'


class AgentDetailView(DetailView):
    model = Agent
    template_name = 'setup/agent/agent_detail.html'
    context_object_name = 'agent'


class AgentCreateView(CreateView):
    model = Agent
    template_name = 'setup/agent/agent_form.html'
    form_class = AgentForm
    #initial = {"email": "Ijaz email"}
    

class AgentUpdateView(UpdateView):
    model = Agent
    template_name = 'setup/agent/agent_form.html'
    form_class = AgentForm
    

class AgentDeleteView(DeleteView):
    model = Agent
    template_name = 'setup/agent/agent_confirm_delete.html'
    context_object_name = 'agent'
    success_url = '/agents/'
    

# -----------------------Doctor Views---------------------------------------


class DoctorListView(ListView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'setup/doctor/doctor_list.html'
    context_object_name = 'doctors'


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'setup/doctor/doctor_detail.html'
    context_object_name = 'doctor'


class DoctorCreateView(CreateView):
    model = Doctor
    template_name = 'setup/doctor/doctor_form.html'
    form_class = DoctorForm
    

class DoctorUpdateView(UpdateView):
    model = Doctor
    template_name = 'setup/doctor/doctor_form.html'
    form_class = DoctorForm
    

class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'setup/doctor/doctor_confirm_delete.html'
    success_url = '/doctors/'
    context_object_name = 'doctor'

# -----------------------Clinic Views---------------------------------------


class ClinicListView(ListView):
    model = Clinic
    form_class = ClinicForm
    template_name = 'setup/clinic/clinic_list.html'
    context_object_name = 'clinics'


class ClinicDetailView(DetailView):
    model = Clinic
    template_name = 'setup/clinic/clinic_detail.html'
    context_object_name = 'clinic'


class ClinicCreateView(CreateView):
    model = Clinic
    template_name = 'setup/clinic/clinic_form.html'
    form_class = ClinicForm
    

class ClinicUpdateView(UpdateView):
    model = Clinic
    template_name = 'setup/clinic/clinic_form.html'
    form_class = ClinicForm
    

class ClinicDeleteView(DeleteView):
    model = Clinic
    template_name = 'setup/clinic/clinic_confirm_delete.html'
    success_url = '/clinics/'
    context_object_name = 'clinic'
    

# -----------------------Source Views---------------------------------------

class SourceListView(ListView):
    model = Source
    form_class = SourceForm
    template_name = 'setup/source/source_list.html'
    context_object_name = 'sources'


class SourceDetailView(DetailView):
    model = Source
    template_name = 'setup/source/source_detail.html'
    context_object_name = 'source'

    def get_context_data(self, *args, **kwargs):
        context = super(SourceDetailView, self).get_context_data(*args, **kwargs)
        #context['rates'] = self.object.rate_set.all().order_by('-amount')  **THis also does the same thing
        context['rates'] = Rate.objects.all().filter(source=self.object).order_by('-amount')
        #context['rates'] = Rate.objects.all().filter(Source=self.kwargs['pk']).order_by('-amount')    **This also does the same thing
        return context


class SourceCreateView(CreateView):
    model = Source
    template_name = 'setup/source/source_form.html'
    form_class = SourceForm
    

class SourceUpdateView(UpdateView):
    model = Source
    template_name = 'setup/source/source_form.html'
    form_class = SourceForm
    

class SourceDeleteView(DeleteView):
    model = Source
    template_name = 'setup/source/source_confirm_delete.html'
    success_url = '/sources/'
    context_object_name = 'source'


# -----------------------Claimant Views---------------------------------------


class ClaimantListView(ListView):
    model = Claimant
    form_class = ClaimantForm
    template_name = 'setup/claimant/claimant_list.html'
    context_object_name = 'claimants'


class ClaimantDetailView(DetailView):
    model = Claimant
    template_name = 'setup/claimant/claimant_detail.html'
    context_object_name = 'claimant'


class ClaimantCreateView(CreateView):
    model = Claimant
    template_name = 'setup/claimant/claimant_form.html'
    form_class = ClaimantForm  
    

class ClaimantUpdateView(UpdateView):
    model = Claimant
    template_name = 'setup/claimant/claimant_form.html'
    form_class = ClaimantForm
    

class ClaimantDeleteView(DeleteView):
    model = Claimant
    template_name = 'setup/claimant/claimant_confirm_delete.html'
    context_object_name = 'claimant'
    success_url = '/claimants/'

# -----------------------Assessment Views---------------------------------------

class AssessmentListView(ListView):
    model = Assessment
    form_class = AssessmentForm
    template_name = 'setup/assessment/assessment_list.html'
    context_object_name = 'assessments'

    
class AssessmentDetailView(DetailView):
    model = Assessment
    template_name = 'setup/assessment/assessment_detail.html'
    context_object_name = 'assessment'

    def get_context_data(self, *args, **kwargs):
        context = super(AssessmentDetailView, self).get_context_data(*args, **kwargs)
        #context['rates'] = self.object.rate_set.all().order_by('-amount')  **THis also does the same thing
        context['invoices'] = Invoice.objects.all().filter(assessment=self.object).order_by('-date')
        context['payments'] = ApplyPayment.objects.filter(assessment=self.kwargs['pk'])
        context['reporttypes'] = ReportType.objects.all()        
        return context

    
class AssessmentCreateView(CreateView):
    model = Assessment
    template_name = 'setup/assessment/assessment_form.html'
    form_class = AssessmentForm     
    

class AssessmentUpdateView(UpdateView):
    model = Assessment
    template_name = 'setup/assessment/assessment_form.html'
    form_class = AssessmentForm
    

class AssessmentDeleteView(DeleteView):
    model = Assessment
    template_name = 'setup/assessment/assessment_confirm_delete.html'
    success_url = '/assessments/'
    context_object_name = 'assessment'

# -----------------------Invoice Views---------------------------------------

class InvoiceListView(ListView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'setup/invoice/invoice_list.html'
    context_object_name = 'invoices'


class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'setup/invoice/invoice_detail.html'    
    context_object_name = 'invoice'


def increment_invoice_number():
    last_invoice = Invoice.objects.all().order_by('id').last()     
    if not last_invoice:        
        return 'EHS1'
    invoice_no = last_invoice.number
    invoice_int = int(invoice_no.split('EHS')[-1])
    new_invoice_int = invoice_int + 1
    new_invoice_no = 'EHS' + str(new_invoice_int)
    return new_invoice_no


def InvoiceCreate(request):
    if request.method == 'POST':        
        form = InvoiceForm(request.POST)        
        if form.is_valid():
   	        form.save()
        return redirect('invoices-list')            
    else:
        reporttype_id = request.GET.get('reporttype_id')
        assessment_id = request.GET.get('assessment_id')        
        source_id = request.GET.get('source_id')
        rate = Rate.objects.get(source=source_id, report_type=reporttype_id)

        amount = rate.amount
        tax = round(amount * Decimal(0.13),2)
        total = amount + tax        
        today = date.today()
        number = increment_invoice_number()        
        form = InvoiceForm(initial={
            'date': today,
            'number': number,
            'subtotal': amount,
            'report_type': reporttype_id,
            'assessment': assessment_id,
            'tax': tax,
            'total': total
        })
    return render(request,'setup/invoice/invoice_form.html',{'form':form})
            

class InvoiceUpdateView(UpdateView):
    model = Invoice
    template_name = 'setup/invoice/invoice_form.html'
    form_class = InvoiceForm

class InvoiceDeleteView(DeleteView):
    model = Invoice
    template_name = 'setup/invoice/assessment_confirm_delete.html'
    success_url = '/invoices/'
    context_object_name = 'invoice'

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
    #initial = {"email": "Ijaz email"}
    

class RateUpdateView(UpdateView):
    model = Rate
    template_name = 'setup/rate_form.html'
    form_class = RateForm
    

class RateDeleteView(DeleteView):
    model = Rate
    template_name = 'setup/rate_confirm_delete.html'
    context_object_name = 'rate'
    success_url = '/rates/'
    

# -----------------------Source Payment Views---------------------------------------
    

class SourcePaymentListView(ListView):
    model = SourcePayment
    form_class = SourcePaymentForm    
    template_name = 'setup/sourcepayment/sourcepayment_list.html'
    context_object_name = 'sourcepayment'


class SourcePaymentDetailView(DetailView):
    model = SourcePayment
    template_name = 'setup/sourcepayment/sourcepayment_detail.html'
    context_object_name = 'sourcepayment'


class SourcePaymentCreateView(CreateView):
    model = SourcePayment
    template_name = 'setup/sourcepayment/sourcepayment_form.html'
    form_class = SourcePaymentForm
    #initial = {"email": "Ijaz email"}
    

class SourcePaymentUpdateView(UpdateView):
    model = SourcePayment
    template_name = 'setup/sourcepayment/sourcepayment_form.html'
    form_class = SourcePaymentForm
    

class SourcePaymentDeleteView(DeleteView):
    model = SourcePayment
    template_name = 'setup/sourcepayment/sourcepayment_confirm_delete.html'
    context_object_name = 'sourcepayment'
    success_url = '/sourcepayments/'
    

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
    #initial = {"email": "Ijaz email"}
    

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
    abr = assessment.report_type.abbreviation
    if abr == 'IME':
        bill = assessment.doctor.rate_ime
    elif abr == 'AD':
        bill = assessment.doctor.rate_ad
    elif abr == 'PR':
        bill = assessment.doctor.rate_pr
    elif abr == 'NS':
        bill = assessment.doctor.rate_ns
    elif abr == 'EX':
        bill = assessment.doctor.rate_ex
    elif abr == 'AR':
        bill = assessment.doctor.rate_ar

    doctorbill = DoctorBill(assessment=assessment, bill_subtotal=bill)
    doctorbill.save()
    return


def CreateAgentInvoice(assessment_id):
    assessment = Assessment.objects.get(id=assessment_id)
    abr = assessment.report_type.abbreviation
    if abr == 'IME':
        bill = assessment.agent.rate_ime
    elif abr == 'AD':
        bill = assessment.agent.rate_ad
    elif abr == 'PR':
        bill = assessment.agent.rate_pr
    elif abr == 'NS':
        bill = assessment.agent.rate_ns
    elif abr == 'EX':
        bill = assessment.agent.rate_ex
        
    agentbill = AgentBill(assessment=assessment, bill_total=bill)
    agentbill.save()
    return


def CreateClinicInvoice(assessment_id):
    assessment = Assessment.objects.get(id=assessment_id)
    abr = assessment.report_type.abbreviation
    if abr == 'IME':
        bill = assessment.clinic.rate_ime
    elif abr == 'NS':
        bill = assessment.clinic.rate_ns
    else:
        return

    clinicbill = ClinicBill(assessment=assessment, bill_total=bill)
    clinicbill.save()
    return


def InvoicePaidSwitch(invoice_id):
    invoice = Assessment.objects.get(id=invoice_id)
    invoice_total = invoice.invoice_total    
    applied_invoices = ApplyPayment.objects.filter(assessment=invoice_id)    
    applied_total = applied_invoices.aggregate(Sum('amount'))["amount__sum"]
       
    if invoice_total == applied_total:
        invoice.invoice_paid = True
        # CreateDoctorInvoice(invoice_id)
        # CreateAgentInvoice(invoice_id)
        # CreateClinicInvoice(invoice_id)
    else:
        invoice.invoice_paid = False
    invoice.save()    
    return  
    

def ProcessPayment(request, pk):
    sourcepayment = Payment.objects.get(id=pk)

    openinvoices = Assessment.objects.filter(claimant__source=sourcepayment.source, invoice_paid = False)
    closedinvoices = Assessment.objects.filter(claimant__source=sourcepayment.source, invoice_paid = True)

    applied = ApplyPayment.objects.filter(payment=pk)
    
    if applied:
        total_applied = applied.aggregate(Sum('amount'))["amount__sum"]
    else:
        total_applied = 0    

    balance = sourcepayment.amount - total_applied

    if request.method == 'POST':
        invoice_id=request.POST.get('invoice_id')
        amount = Decimal(request.POST.get('amount'))
        if amount > balance:
            messages.error(request, 'Applied amount is greater than Balance remaining')
            return redirect('process', pk)

        assessment = Assessment.objects.get(id=invoice_id)

        if amount > assessment.invoice_total:
            messages.error(request, 'Applied amount cannot be higher than invoice amount')
            return redirect('process', pk)
        
        if amount < assessment.invoice_total:
            messages.warning(request, 'Partial Payment Applied')
            applypayment = ApplyPayment(assessment=assessment, payment=sourcepayment, amount=amount)
            applypayment.save()
            return redirect('process', pk)
        
        if amount == assessment.invoice_total:
            messages.info(request, 'Applied')
            applypayment = ApplyPayment(assessment=assessment, payment=sourcepayment, amount=amount)
            applypayment.save()
            # InvoicePaidSwitch(invoice_id)
            return redirect('process', pk)

    context = {
        'openinvoices': openinvoices,
        'closedinvoices': closedinvoices,
        'payment': sourcepayment,
        'total_applied': total_applied,
        'balance': balance,        
    }       
    return render(request, 'setup/processpayment.html', context)


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
#     total_applied = applied.aggregate(Sum('amount'))    
    
#     if 'search' in request.GET:
#         search = request.GET['search'] 
#         #find all invoices in Assessments with invoice#=search AND Source company with above Payment pk       
#         invoice_search = Assessment.objects.get(invoice_number=search, Source=payment.Source)
                
#         if invoice_search is not None:

#             if ApplyPayment.objects.filter(assessment=invoice_search):
#                 if invoice_search.invoice_paid == True:
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
#             x = form.cleaned_data['amount']            
#             z = Assessment.objects.get(id=applypayment_assessment.id).invoice_total          

#             if x > z:
#                 messages.error(request, 'Applied amount cannot be higher than invoice amount')
#                 return redirect('process', pk)
            
#             form.save()                        
#             invoice_paidSwitch(applypayment_assessment.id)            
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
