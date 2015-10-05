from django.contrib import admin
from jobs_dash.models import Job, Comment, Issue
from datetime import datetime
today = datetime.today().date()

def make_invoiced(modeladmin, request, queryset):
	queryset.update(is_open = False)
	queryset.update(is_invoiced = True)
	queryset.update(invoiced_date = today)
make_invoiced.short_description = "Invoice and close selected jobs"


class JobAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('address',)}
	list_display = ('address', 'due_date', 'invoiced_date', 'is_open', 'is_invoiced', 'is_paid')
	list_filter = ["due_date"]
	search_fields = ['address']
	actions = [make_invoiced]
	fieldsets = [
		('House', 			{'fields': ['address', 'due_date', 'price', 'pic']}),
		('PO\'s', 		{'fields': ['purchase_order', 'repair_po', 'paint_po']}),
		('Flooring', 	{'fields': ['flooring', 'flooring_date']}),
		('Agent Info',	{'fields': ['agent_name', 'agent_phone', 'agent_email']}),
		('Invoice',		{'fields': ['is_open', 'is_invoiced', 'invoiced_date', 'is_paid', 'paid_date']}),
		(None,			{'fields': ['slug']}),
	]


admin.site.register(Job, JobAdmin)
admin.site.register(Comment)
admin.site.register(Issue)

