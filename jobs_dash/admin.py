from django.contrib import admin
from jobs_dash.models import Job, Comment

class JobAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('address',)}

admin.site.register(Job, JobAdmin)
admin.site.register(Comment)

