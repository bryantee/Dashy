from django.shortcuts import render
from django.http import HttpResponse
from jobs_dash.models import Job

def index(request):
	jobs_list = Job.objects.order_by('-due_date')

	context_dict = {'open_jobs': jobs_list}
	return render(request, 'jobs_dash/index.html', context_dict)

