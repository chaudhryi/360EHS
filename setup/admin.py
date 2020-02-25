from django.contrib import admin
from .models import Agent, Doctor, Source, Clinic, Assessment, ReportType, Rate, Payment, ApplyPayment, Claimant

admin.site.register(Agent)
admin.site.register(Doctor)
admin.site.register(Clinic)
admin.site.register(Source)
admin.site.register(Payment)
admin.site.register(ApplyPayment)
admin.site.register(Claimant)


class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('report_type', 'clinic', 'doctor', 'agent', 'assessment_date')
    list_filter = ('assessment_date', 'doctor', 'agent')  

admin.site.register(Assessment, AssessmentAdmin)


class RateAdmin(admin.ModelAdmin):
    list_display = ('source', 'report_type', 'amount')
    list_filter = ('source', 'report_type')

admin.site.register(Rate, RateAdmin)


class ReportTypeAdmin(admin.ModelAdmin):
    list_display = ('abbreviation', 'description')

admin.site.register(ReportType, ReportTypeAdmin)


