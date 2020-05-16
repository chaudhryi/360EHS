from django.shortcuts import render, redirect, get_object_or_404
from .models import Assessment, Doctor, Clinic, Agent, Source, Rate, SourcePayment, ApplyPayment, DoctorBill, AgentBill, ClinicBill, Claimant, Invoice, ReportType, Expense, AgentBill, DoctorBill, ClinicBill
from .forms import AgentForm, DoctorForm, ClinicForm, SourceForm, AssessmentForm, InvoiceForm, RateForm, SourcePaymentForm, ApplyPaymentForm, ClaimantForm, ExpenseForm, AgentBillForm, DoctorBillForm, ClinicBillForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from datetime import date
from django.contrib import messages
from django.db.models import Sum
from decimal import Decimal
from operator import attrgetter
from itertools import chain
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy



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

    def get_context_data(self, **kwargs):
        context = super(AgentDetailView, self).get_context_data(**kwargs)
        context['bills'] = AgentBill.objects.filter(invoice__assessment__agent=self.object)
        return context


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
    template_name = 'setup/claimant/claimant_list.html'
    context_object_name = 'claimants'


class ClaimantDetailView(DetailView):
    model = Claimant
    template_name = 'setup/claimant/claimant_detail.html'
    context_object_name = 'claimant'

    def get_context_data(self, *args, **kwargs):
        context = super(ClaimantDetailView, self).get_context_data(*args, **kwargs)
        context['assessments'] = Assessment.objects.all().filter(claimant=self.object).order_by('-date')
        return context


class ClaimantCreateView(CreateView):
    model = Claimant
    template_name = 'setup/claimant/claimant_form.html'
    form_class = ClaimantForm
    success_url = "/claimants/"  
    

class ClaimantUpdateView(UpdateView):
    model = Claimant
    template_name = 'setup/claimant/claimant_form.html'
    form_class = ClaimantForm
    

class ClaimantDeleteView(DeleteView):
    model = Claimant
    template_name = 'setup/claimant/claimant_confirm_delete.html'
    context_object_name = 'claimant'
    
    def get_success_url(self):
        return reverse_lazy('claimants-list')

# -----------------------Assessment Views---------------------------------------

class AssessmentListView(ListView):
    model = Assessment    
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


def AssessmentCreate(request):
    if request.method == 'POST':        
        form = AssessmentForm(request.POST)        
        if form.is_valid():
   	        assessment = form.save()
        return redirect('assessments-detail',assessment.id)            
    else:
        claimant_id = request.GET.get('claimant_id')
        form = AssessmentForm(initial={'claimant': claimant_id})
    return render(request,'setup/assessment/assessment_form.html',{'form':form}) 


class AssessmentUpdateView(UpdateView):
    model = Assessment
    template_name = 'setup/assessment/assessment_form.html'
    form_class = AssessmentForm

    

class AssessmentDeleteView(DeleteView):
    model = Assessment
    template_name = 'setup/assessment/assessment_confirm_delete.html'
    success_url = '/assessments/'
    context_object_name = 'assessment'

    def get_success_url(self):
        return reverse_lazy('claimants-detail', kwargs={'pk': self.object.claimant_id})

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
    assessment_id = request.GET.get('assessment_id')
    reporttype_id = request.GET.get('reporttype_id')
    source_id = request.GET.get('source_id')

    if request.method == 'POST':        
        form = InvoiceForm(request.POST)
        # form.fields['report_type'].disabled = True
        # form.fields['assessment'].disabled = True        
        if form.is_valid():
   	        invoice = form.save()
        CreateAgentInvoice(invoice.id)
        CreateClinicInvoice(invoice.id)
        return redirect('assessments-detail', assessment_id)
    else:
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
        # form.fields['report_type'].disabled = True
        # form.fields['assessment'].disabled = True

    return render(request,'setup/invoice/invoice_form.html',{'form':form})
            

class InvoiceUpdateView(UpdateView):
    model = Invoice
    template_name = 'setup/invoice/invoice_form.html'
    form_class = InvoiceForm


class InvoiceDeleteView(DeleteView):
    model = Invoice
    template_name = 'setup/invoice/invoice_confirm_delete.html'
    success_url = '/invoices/'
    context_object_name = 'invoice'

    def get_success_url(self):
        return reverse_lazy('assessments-detail', kwargs={'pk': self.object.assessment_id})

# -----------------------Rate Views---------------------------------------
    

class RateListView(ListView):
    model = Rate       
    template_name = 'setup/rate/rate_list.html'
    context_object_name = 'rates'
    ordering = ['source']


class RateDetailView(DetailView):
    model = Rate
    template_name = 'setup/rate/rate_detail.html'
    context_object_name = 'rate'


class RateCreateView(CreateView):
    model = Rate
    template_name = 'setup/rate/rate_form.html'
    form_class = RateForm
    #initial = {"email": "Ijaz email"}
    

class RateUpdateView(UpdateView):
    model = Rate
    template_name = 'setup/rate/rate_form.html'
    form_class = RateForm
    

class RateDeleteView(DeleteView):
    model = Rate
    template_name = 'setup/rate/rate_confirm_delete.html'
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
    doctor = invoice.assessment.doctor

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
    
    doctorbill = DoctorBill(invoice=invoice, doctor=doctor, subtotal=bill)
    doctorbill.save()
    return


def CreateAgentInvoice(invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    abr = invoice.report_type.abbreviation
    agent = invoice.assessment.agent

    if abr == 'IME':
        bill = invoice.assessment.agent.rate_ime
    elif abr == 'AD':
        bill = invoice.assessment.agent.rate_ad
    elif abr == 'PR':
        bill = invoice.assessment.agent.rate_pr
    elif abr == 'NS':
        bill = invoice.assessment.agent.rate_ns
    elif abr == 'EX':
        bill = invoice.assessment.agent.rate_ex
    elif abr == 'AR':
        bill = invoice.assessment.agent.rate_ar
        
    agentbill = AgentBill(invoice=invoice, agent=agent, total=bill)
    agentbill.save()
    return


def CreateClinicInvoice(invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    abr = invoice.report_type.abbreviation
    clinic = invoice.assessment.clinic

    if abr == 'IME':
        bill = invoice.assessment.clinic.rate_ime
    elif abr == 'NS':
        bill = invoice.assessment.clinic.rate_ns
    else:
        return

    clinicbill = ClinicBill(invoice=invoice, clinic=clinic, total=bill)
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
                'total': total,
                'subtotal': subtotal,
                'tax': tax,
                'count': count,
                'physician': physician,
            }
            context.update(newcontext)

        if 'paydoctor_id' in request.POST:
            doctor_id = request.POST.get('paydoctor_id')
            physician = Doctor.objects.get(id=doctor_id)
            reference = request.POST.get('reference')
            doctorbills = DoctorBill.objects.filter(invoice__assessment__doctor=doctor_id, paid=False)
            payee = physician
            total = doctorbills.aggregate(Sum('total'))["total__sum"]
            subtotal = doctorbills.aggregate(Sum('subtotal'))["subtotal__sum"]
            tax = doctorbills.aggregate(Sum('tax'))["tax__sum"]
            description = 'Physician payout'

            expense = Expense(
                reference = reference,
                description = description,
                payee = payee,
                subtotal = subtotal,
                tax = tax,
                total = total,
                doctor = physician
                )
            expense.save()
            
            for bill in doctorbills:
                bill.paid = True
                bill.expense = expense
                bill.paid_date = date.today()
                bill.save()
            

    return render(request, 'setup/paydoctors.html', context)


def PayAgents(request):
    agents = Agent.objects.all()
    context = {'agents': agents}
      

    if request.method == 'POST':
        if 'agent_id' in request.POST:
            agent_id = request.POST.get('agent_id')
            agent = Agent.objects.get(id=agent_id)
            agentbills = AgentBill.objects.filter(invoice__assessment__agent=agent_id, paid=False)
            total = agentbills.aggregate(Sum('total'))["total__sum"]
            count = agentbills.count()

            newcontext = {
                'agentbills': agentbills,                
                'total': total,
                'count': count,
                'agent': agent,
            }
            context.update(newcontext)

        if 'payagent_id' in request.POST:
            agent_id = request.POST.get('payagent_id')
            agent = Agent.objects.get(id=agent_id)
            reference = request.POST.get('reference')
            agentbills = AgentBill.objects.filter(invoice__assessment__agent=agent_id, paid=False)
            payee = agent
            total = agentbills.aggregate(Sum('total'))["total__sum"]
            description = 'Agent payout'

            expense = Expense(
                reference = reference,
                description = description,
                tax = '0.00',
                payee = payee,
                total = total,
                agent = agent
                )
            expense.save()
            
            for bill in agentbills:
                bill.paid = True
                bill.expense = expense
                bill.paid_date = date.today()
                bill.save()

    return render(request, 'setup/payagents.html', context)


def PayClinics(request):
    clinics = Clinic.objects.all()
    context = {'clinics': clinics}
      

    if request.method == 'POST':
        if 'clinic_id' in request.POST:
            clinic_id = request.POST.get('clinic_id')
            clinic = Clinic.objects.get(id=clinic_id)
            clinicbills = ClinicBill.objects.filter(invoice__assessment__clinic=clinic_id, paid=False)
            total = clinicbills.aggregate(Sum('total'))["total__sum"]
            count = clinicbills.count()

            newcontext = {
                'clinicbills': clinicbills,                
                'total': total,
                'count': count,
                'clinic': clinic,
            }
            context.update(newcontext)

        if 'payclinic_id' in request.POST:
            clinic_id = request.POST.get('payclinic_id')
            clinic = Clinic.objects.get(id=clinic_id)
            reference = request.POST.get('reference')
            clinicbills = ClinicBill.objects.filter(invoice__assessment__clinic=clinic_id, paid=False)
            payee = clinic
            total = clinicbills.aggregate(Sum('total'))["total__sum"]
            description = 'Clinic payout'

            expense = Expense(
                reference = reference,
                description = description,
                tax = '0.00',
                payee = payee,
                total = total,
                clinic = clinic
                )
            expense.save()
            
            for bill in clinicbills:
                bill.paid = True
                bill.expense = expense
                bill.paid_date = date.today()
                bill.save()

    return render(request, 'setup/payclinics.html', context)

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

    def get_context_data(self, **kwargs):
        context = super(ExpenseDetailView, self).get_context_data(**kwargs)
        context['agentbills'] = AgentBill.objects.filter(expense=self.object)
        context['doctorbills'] = DoctorBill.objects.filter(expense=self.object)        
        return context


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


# -----------------------AgentBill Views---------------------------------------

class AgentBillListView(ListView):
    model = AgentBill    
    template_name = 'setup/agentbill/agentbill_list.html'
    context_object_name = 'agentbills'


class AgentBillDetailView(DetailView):
    model = AgentBill
    template_name = 'setup/agentbill/agentbill_detail.html'
    context_object_name = 'agentbill'


class AgentBillCreateView(CreateView):
    model = AgentBill
    template_name = 'setup/agentbill/agentbill_form.html'
    form_class = AgentBillForm  


class AgentBillUpdateView(UpdateView):
    model = AgentBill
    template_name = 'setup/agentbill/agentbill_form.html'
    form_class = AgentBillForm


class AgentBillDeleteView(DeleteView):
    model = AgentBill
    template_name = 'setup/agentbill/agentbill_confirm_delete.html'
    context_object_name = 'agentbill'

    def get_success_url(self):
        return reverse_lazy('agentbills-list')

# -----------------------DoctorBill Views---------------------------------------

class DoctorBillListView(ListView):
    model = DoctorBill    
    template_name = 'setup/doctorbill/doctorbill_list.html'
    context_object_name = 'doctorbills'


class DoctorBillDetailView(DetailView):
    model = DoctorBill
    template_name = 'setup/doctorbill/doctorbill_detail.html'
    context_object_name = 'doctorbill'


class DoctorBillCreateView(CreateView):
    model = DoctorBill
    template_name = 'setup/doctorbill/doctorbill_form.html'
    form_class = DoctorBillForm  


class DoctorBillUpdateView(UpdateView):
    model = DoctorBill
    template_name = 'setup/doctorbill/doctorbill_form.html'
    form_class = DoctorBillForm


class DoctorBillDeleteView(DeleteView):
    model = DoctorBill
    template_name = 'setup/doctorbill/doctorbill_confirm_delete.html'
    context_object_name = 'doctorbill'

    def get_success_url(self):
        return reverse_lazy('doctorbills-list')

# -----------------------ClinicBill Views---------------------------------------

class ClinicBillListView(ListView):
    model = ClinicBill    
    template_name = 'setup/clinicbill/clinicbill_list.html'
    context_object_name = 'clinicbills'


class ClinicBillDetailView(DetailView):
    model = ClinicBill
    template_name = 'setup/clinicbill/clinicbill_detail.html'
    context_object_name = 'clinicbill'


class ClinicBillCreateView(CreateView):
    model = ClinicBill
    template_name = 'setup/clinicbill/clinicbill_form.html'
    form_class = ClinicBillForm  


class ClinicBillUpdateView(UpdateView):
    model = ClinicBill
    template_name = 'setup/clinicbill/clinicbill_form.html'
    form_class = ClinicBillForm


class ClinicBillDeleteView(DeleteView):
    model = ClinicBill
    template_name = 'setup/clinicbill/clinicbill_confirm_delete.html'
    context_object_name = 'clinicbill'

    def get_success_url(self):
        return reverse_lazy('clinicbills-list')


def Ledger(request):
    debit = Expense.objects.only('date', 'total', 'abbreviation', 'description')
    if debit:
        total_debit = debit.aggregate(Sum('total'))["total__sum"]
        total_debit_tax = debit.aggregate(Sum('tax'))["tax__sum"]
    else:
        total_debit = 0
        total_debit_tax = 0

    credit = SourcePayment.objects.only('date', 'amount', 'abbreviation', 'source')
    if credit:
        total_credit = credit.aggregate(Sum('amount'))["amount__sum"]
        total_credit_tax = credit.aggregate(Sum('tax'))["tax__sum"]
    else:
        total_credit = 0
        total_credit_tax = 0

    combined = sorted(chain(debit, credit),key=attrgetter('date'), reverse=True)
    balance = (total_credit-total_debit) + (total_credit_tax - total_debit_tax)

    context = {
        'combined': combined,
        'total_debit': total_debit,
        'total_credit': total_credit,
        'total_debit_tax': total_debit_tax,
        'total_credit_tax': total_credit_tax,
        'balance': balance,
    }
    return render(request, 'setup/ledger.html', context)









