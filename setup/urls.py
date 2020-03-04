from django.urls import path
from .views import AgentListView, AgentDetailView, AgentCreateView, AgentUpdateView, AgentDeleteView, DoctorListView, DoctorDetailView, DoctorCreateView, DoctorUpdateView, DoctorDeleteView, ClinicListView, ClinicCreateView, ClinicDetailView, ClinicUpdateView, ClinicDeleteView, SourceListView, SourceCreateView, SourceDetailView, SourceUpdateView, SourceDeleteView, AssessmentListView, AssessmentCreateView, AssessmentDetailView, AssessmentUpdateView, AssessmentDeleteView, InvoiceListView, InvoiceCreate, InvoiceDetailView, InvoiceUpdateView, InvoiceDeleteView, RateListView, RateDetailView, RateCreateView,RateUpdateView, RateDeleteView, SourcePaymentListView, SourcePaymentDetailView, SourcePaymentCreateView, SourcePaymentUpdateView, SourcePaymentDeleteView, ApplyPaymentListView, ApplyPaymentDetailView, ApplyPaymentCreateView, ApplyPaymentUpdateView, ApplyPaymentDeleteView, ProcessPayment, ClaimantListView, ClaimantDetailView, ClaimantCreateView, ClaimantUpdateView, ClaimantDeleteView
from . import views


urlpatterns = [
    path('', views.Index, name='index'),
    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
    
#---------------Agents URLs------------------------------------------
    path('agents/', AgentListView.as_view(), name='agents-list'),
    path('agents/new/', AgentCreateView.as_view(), name='agents-new'),
    path('agents/<int:pk>/', AgentDetailView.as_view(), name='agents-detail'),
    path('agents/<int:pk>/update/', AgentUpdateView.as_view(), name='agents-update'),
    path('agents/<int:pk>/delete/', AgentDeleteView.as_view(), name='agents-delete'),

#---------------Doctors URLs-----------------------------------------
    path('doctors/', DoctorListView.as_view(), name='doctors-list'),
    path('doctors/new/', DoctorCreateView.as_view(), name='doctors-new'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctors-detail'),
    path('doctors/<int:pk>/update/', DoctorUpdateView.as_view(), name='doctors-update'),
    path('doctors/<int:pk>/delete/', DoctorDeleteView.as_view(), name='doctors-delete'),

#---------------Clinics URLs-----------------------------------------
    path('clinics/', ClinicListView.as_view(), name='clinics-list'),
    path('clinics/new/', ClinicCreateView.as_view(), name='clinics-new'),
    path('clinics/<int:pk>/', ClinicDetailView.as_view(), name='clinics-detail'),
    path('clinics/<int:pk>/update/', ClinicUpdateView.as_view(), name='clinics-update'),
    path('clinics/<int:pk>/delete/', ClinicDeleteView.as_view(), name='clinics-delete'),

#---------------Sources URLs-----------------------------------------
    path('sources/', SourceListView.as_view(), name='sources-list'),
    path('sources/new/', SourceCreateView.as_view(), name='sources-new'),
    path('sources/<int:pk>/', SourceDetailView.as_view(), name='sources-detail'),
    path('sources/<int:pk>/update/', SourceUpdateView.as_view(), name='sources-update'),
    path('sources/<int:pk>/delete/', SourceDeleteView.as_view(), name='sources-delete'),

#---------------Claimant URLs------------------------------------------
    path('claimants/', ClaimantListView.as_view(), name='claimants-list'),
    path('claimants/new/', ClaimantCreateView.as_view(), name='claimants-new'),
    path('claimants/<int:pk>/', ClaimantDetailView.as_view(), name='claimants-detail'),
    path('claimants/<int:pk>/update/', ClaimantUpdateView.as_view(), name='claimants-update'),
    path('claimants/<int:pk>/delete/', ClaimantDeleteView.as_view(), name='claimants-delete'),

#---------------Assessment URLs--------------------------------------
    path('assessments/', AssessmentListView.as_view(), name='assessments-list'),
    path('assessments/new/', AssessmentCreateView.as_view(), name='assessments-new'),
    path('assessments/<int:pk>/', AssessmentDetailView.as_view(), name='assessments-detail'),
    path('assessments/<int:pk>/update/', AssessmentUpdateView.as_view(), name='assessments-update'),
    path('assessments/<int:pk>/delete/', AssessmentDeleteView.as_view(), name='assessments-delete'),

#---------------Invoice URLs-----------------------------------------
    path('invoices/', InvoiceListView.as_view(), name='invoices-list'),
    # path('invoices/new/', InvoiceCreateView.as_view(), name='invoices-new'),
    path('invoices/new/', views.InvoiceCreate, name='invoices-new'),
    path('invoices/<int:pk>/', InvoiceDetailView.as_view(), name='invoices-detail'),       
    path('invoices/<int:pk>/update/', InvoiceUpdateView.as_view(), name='invoices-update'),
    path('invoices/<int:pk>/delete/', InvoiceDeleteView.as_view(), name='invoices-delete'),

#---------------Rates URLs-------------------------------------------  
    path('rates/', RateListView.as_view(), name='rates-list'),
    path('rates/new/', RateCreateView.as_view(), name='rates-new'),
    path('rates/<int:pk>/', RateDetailView.as_view(), name='rates-detail'),
    path('rates/<int:pk>/update/', RateUpdateView.as_view(), name='rates-update'),
    path('rates/<int:pk>/delete/', RateDeleteView.as_view(), name='rates-delete'),

#---------------SourcePayments URLs-------------------------------------------  
    path('sourcepayments/', SourcePaymentListView.as_view(), name='sourcepayments-list'),
    path('sourcepayments/new/', SourcePaymentCreateView.as_view(), name='sourcepayments-new'),
    path('sourcepayments/<int:pk>/', SourcePaymentDetailView.as_view(), name='sourcepayments-detail'),
    path('sourcepayments/<int:pk>/update/', SourcePaymentUpdateView.as_view(), name='sourcepayments-update'),
    path('sourcepayments/<int:pk>/delete/', SourcePaymentDeleteView.as_view(), name='sourcepayments-delete'),

#---------------ApplyPayments URLs-------------------------------------------  
    path('applypayments/', ApplyPaymentListView.as_view(), name='applypayments-list'),
    path('applypayments/new/', ApplyPaymentCreateView.as_view(), name='applypayments-new'),
    path('applypayments/<int:pk>/', ApplyPaymentDetailView.as_view(), name='applypayments-detail'),
    path('applypayments/<int:pk>/update/', ApplyPaymentUpdateView.as_view(), name='applypayments-update'),
    path('applypayments/<int:pk>/delete/', ApplyPaymentDeleteView.as_view(), name='applypayments-delete'),

    path('process/<int:pk>/', views.ProcessPayment, name='process'),

]
