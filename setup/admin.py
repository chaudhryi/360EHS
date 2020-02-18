from django.contrib import admin

from .models import Agent, Doctor, Source, Clinic, Assessment, ReportType, Rate, Payment, ApplyPayment
admin.site.register(Agent)
admin.site.register(Doctor)
admin.site.register(Clinic)
admin.site.register(Source)
admin.site.register(Payment)
admin.site.register(ApplyPayment)




class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('Claimant_Name', 'Source', 'Report_Type',
                    'Clinic', 'Doctor', 'Agent', 'AssessmentDate')
    list_filter = ('AssessmentDate', 'Doctor', 'Agent')
    search_fields = ['Claimant_Name']


admin.site.register(Assessment, AssessmentAdmin)


class RateAdmin(admin.ModelAdmin):
    list_display = ('Source', 'Report_Type', 'Amount')
    list_filter = ('Source', 'Report_Type')


admin.site.register(Rate, RateAdmin)


class ReportTypeAdmin(admin.ModelAdmin):
    list_display = ('Abbreviation', 'Description')


admin.site.register(ReportType, ReportTypeAdmin)


