from django.shortcuts import render
from django.http import HttpResponse
from jobs_dash.models import Job
from datetime import datetime

def index(request):
	jobs_list = Job.objects.order_by('due_date')
	context_dict = {'open_jobs': jobs_list}

	return render(request, 'jobs_dash/index.html', context_dict)

def job_detail(request, job_address_slug):
	context_dict = {}

	try:
		# .get job instance or raise exception DoesNotExist
		job = Job.objects.get(slug=job_address_slug)
		context_dict['job_address'] = job.address

	except Job.DoesNotExist:
		pass

	# gets attributes
	context_dict['job_date_created'] = job.date_created
	context_dict['job_due_date'] = job.due_date
	context_dict['job_price'] = job.price

	#expirimental - get comments
	comment_list = job.comment_set.all().order_by('date')
	context_dict['comments'] = comment_list

	# Show current issues
	# Future plans for link to more details on issues and past issues
	issues_list = job.issue_set.all()
	issues_count = len(issues_list)
	context_dict['issues_count'] = issues_count
	context_dict['issues_list'] = issues_list

	# Calculates days left until project due	
	today = datetime.today().date()
	dt = job.due_date - today
	context_dict['dt'] = dt

	return render(request, 'jobs_dash/job_detail.html', context_dict)
