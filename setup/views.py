from django.shortcuts import render, redirect, get_object_or_404
from .models import Assessment, Doctor, Clinic, Agent, Source, Rate, SourcePayment, ApplyPayment, DoctorBill, AgentBill, ClinicBill, Claimant, Invoice, ReportType, Expense
from .forms import AgentForm, DoctorForm, ClinicForm, SourceForm, AssessmentForm, InvoiceForm, RateForm, SourcePaymentForm, ApplyPaymentForm, ClaimantForm, ExpenseForm
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
        context['invoices'] = Invoice.objects.all().filter(assessment=self.object).order_by('-date')
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
    template_name = 'setup/applypayment/applypayment_list.html'
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


# -----------------------Create Invoice Views---------------------------------------

def CreateDoctorInvoice(invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    abr = invoice.report_type.abbreviation
    if abr == 'IME':
        bill = invoice.assessment.doctor.rate_ime
    elif abr == 'AD':
        bill = invoice.assessment.doctor.rate_ad
    elif abr == 'PR':
        bill = invoice.assessment.doctor.rate_pr
    elif abr == 'NS':
        bill = invoice.assessment.doctor.rate_ns
    elif abr == 'EX':
        bill = invoice.assessment.doctor.rate_ex
    elif abr == 'AR':
        bill = invoice.assessment.doctor.rate_ar

    doctorbill = DoctorBill(invoice=invoice, subtotal=bill)
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
    invoice = Invoice.objects.get(id=invoice_id)
    invoice_total = invoice.total    
    applied_invoices = ApplyPayment.objects.filter(invoice=invoice_id)
    if applied_invoices:            
        applied_total = applied_invoices.aggregate(Sum('amount'))["amount__sum"]
    else:
        applied_total = 0
       
    if applied_total == invoice_total:
        invoice.paid = True
        CreateDoctorInvoice(invoice_id)
        
    if applied_total < invoice_total:
        invoice.paid = False
        bill = DoctorBill.objects.filter(invoice=invoice_id)
        
        if bill:
            bill.delete()
        
    invoice.save()    
    return  
    
# -----------------------Process Source Payments Views---------------------------------------

def ProcessPayment(request, pk):
    source_payment = SourcePayment.objects.get(id=pk)
    open_invoices = Invoice.objects.filter(assessment__claimant__source=source_payment.source, paid = False)    
    applied = ApplyPayment.objects.filter(sourcepayment=pk)
    
    if applied:
        total_applied = applied.aggregate(Sum('amount'))["amount__sum"]
    else:
        total_applied = 0    

    balance = source_payment.amount - total_applied

    if request.method == 'POST':
        invoice_id=request.POST.get('invoice_id')
        invoice = Invoice.objects.get(id=invoice_id)
        amount = Decimal(request.POST.get('amount'))

        if amount > balance:
            messages.error(request, 'Applied amount is greater than Balance remaining')
            return redirect('process', pk)

        if amount > invoice.balance:
            messages.error(request, 'Applied amount cannot be higher than invoice balance')
            return redirect('process', pk)
        
        if amount < invoice.balance:
            messages.warning(request, 'Partial Payment Applied')

        if amount == invoice.total:
            messages.info(request, 'Applied Fully')

        applypayment = ApplyPayment(invoice=invoice, sourcepayment=source_payment, amount=amount)
        applypayment.save()
        invoice.applied=invoice.applied + amount
        invoice.save()
        InvoicePaidSwitch(invoice_id)
        return redirect('process', pk)

    context = {
        'openinvoices': open_invoices,
        'applied': applied,        
        'payment': source_payment,
        'total_applied': total_applied,
        'balance': balance,        
    }       
    return render(request, 'setup/processpayment.html', context)


def ReversePayment(request, item_id):
        
    payment_to_delete = ApplyPayment.objects.get(id=item_id)
    invoice_id = payment_to_delete.invoice.id
    pk = payment_to_delete.sourcepayment.id
    amount = payment_to_delete.amount
    payment_to_delete.delete()
    invoice = Invoice.objects.get(id=invoice_id)
    invoice.applied = invoice.applied - amount
    invoice.save()
    InvoicePaidSwitch(invoice_id)

    return redirect('process', pk)

# -----------------------Pay Doctors / Agents / Clinics Views---------------------------------------

def PayDoctors(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}  

    # if request.method == 'POST':

    #     return render(request, 'setup/paydoctors.html', context)

    if request.method == 'POST':
        if 'doctor_id' in request.POST:
            doctor_id = request.POST.get('doctor_id')
            physician = Doctor.objects.get(id=doctor_id)
            doctorbills = DoctorBill.objects.filter(invoice__assessment__doctor=doctor_id, paid=False)
            total = doctorbills.aggregate(Sum('total'))["total__sum"]
            subtotal = doctorbills.aggregate(Sum('subtotal'))["subtotal__sum"]
            tax = doctorbills.aggregate(Sum('tax'))["tax__sum"]
            count = doctorbills.count()

            newcontext = {
                'doctorbills': doctorbills,
                'date': date.today(),
                'total': total,
                'subtotal': subtotal,
                'tax': tax,
                'count': count,
                'physician': physician,
            }
            context.update(newcontext)

    return render(request, 'setup/paydoctors.html', context)

# -----------------------Expense Views---------------------------------------

class ExpenseListView(ListView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'setup/expense/expense_list.html'
    context_object_name = 'expenses'


class ExpenseDetailView(DetailView):
    model = Expense
    template_name = 'setup/expense/expense_detail.html'
    context_object_name = 'expense'


class ExpenseCreateView(CreateView):
    model = Expense
    template_name = 'setup/expense/expense_form.html'
    form_class = ExpenseForm  


class ExpenseUpdateView(UpdateView):
    model = Expense
    template_name = 'setup/expense/expense_form.html'
    form_class = ExpenseForm

class ExpenseDeleteView(DeleteView):
    model = Expense
    template_name = 'setup/expense/expense_confirm_delete.html'
    context_object_name = 'expense'
    success_url = '/expenses/'








