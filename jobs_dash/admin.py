from django.contrib import admin
from jobs_dash.models import Job, Comment, Issue
from datetime import date
today = date.today()

def make_invoiced(modeladmin, request, queryset):
	queryset.update(is_open = False)
	queryset.update(is_invoiced = True)
	queryset.update(invoiced_date = today)
make_invoiced.short_description = "Invoice and close selected jobs"


class JobAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('address',)}
	list_display = ('address', 'due_date', 'is_open', 'is_invoiced', 'invoiced_date')
	list_filter = ["due_date"]
	search_fields = ['address']
	actions = [make_invoiced]


admin.site.register(Job, JobAdmin)
admin.site.register(Comment)
admin.site.register(Issue)

