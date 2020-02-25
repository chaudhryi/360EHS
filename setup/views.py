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
    #initial = {"email": "Ijaz email"}
    

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
        #context['rates'] = self.object.rate_set.all().order_by('-amount')  **THis also does the same thing
        context['rates'] = Rate.objects.all().filter(source=self.object).order_by('-amount')
        #context['rates'] = Rate.objects.all().filter(Source=self.kwargs['pk']).order_by('-amount')    **This also does the same thing
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
        #context['rates'] = self.object.rate_set.all().order_by('-amount')  **THis also does the same thing
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
            invoices = Assessment.objects.filter(invoice_number=search)
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
    # initial = {"invoice_subtotal": '500'}
    
    def get_context_data(self, *args, **kwargs):
        context = super(InvoiceCreateView, self).get_context_data(**kwargs) 
        source_pk = self.kwargs['source_pk']
        report_pk = self.kwargs['report_pk']               
        context['hold'] = Rate.objects.get(source=source_pk, report_type=report_pk)
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
    #initial = {"email": "Ijaz email"}
    

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
    abr = assessment.report_type.Abbreviation
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


def invoice_paidSwitch(invoice_id):
    invoice = Assessment.objects.get(id=invoice_id)
    invoice_total = invoice.invoice_total    
    applied_invoices = ApplyPayment.objects.filter(assessment=invoice_id)    
    applied_total = applied_invoices.aggregate(Sum('amount'))["amount__sum"]
       
    if invoice_total == applied_total:
        invoice.invoice_paid = True
        CreateDoctorInvoice(invoice_id)
        CreateAgentInvoice(invoice_id)
        CreateClinicInvoice(invoice_id)
    else:
        invoice.invoice_paid = False
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

def ProcessPayment(request, pk):
    sourcepayment = Payment.objects.get(id=pk)

    openinvoices = Assessment.objects.filter(claimant__source=sourcepayment.source, invoice_paid = False)
    closedinvoices = Assessment.objects.filter(claimant__source=sourcepayment.source, invoice_paid = True)

    applied = ApplyPayment.objects.filter(payment=pk)
    
    if applied:
        total_applied = applied.aggregate(Sum('amount'))
        subtract = total_applied["amount__sum"]
    else:
        subtract = 0    

    balance = sourcepayment.amount - subtract

    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = ApplyPaymentForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            applypayment_assessment = form.cleaned_data['assessment']
            x = form.cleaned_data['amount']            
            z = Assessment.objects.get(id=applypayment_assessment.id).invoice_total          

            if x > z:
                messages.error(request, 'Applied amount cannot be higher than invoice amount')
                return redirect('process', pk)
            
            form.save()                        
            invoice_paidSwitch(applypayment_assessment.id)            
            return redirect('process', pk)           

    # If this is a GET (or any other method) create the default form.
    else:
        form = ApplyPaymentForm()


    context = {
        'form': form,
        'openinvoices': openinvoices,
        'closedinvoices': closedinvoices,
        'payment': sourcepayment,
        'total_applied': subtract,
        'balance': balance,        
                
    }       
    return render(request, 'setup/processpayment.html', context)


    
