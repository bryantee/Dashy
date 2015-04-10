from django.shortcuts import render
from django.http import HttpResponse
from jobs_dash.models import Job

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

		# gets attributes
		context_dict['job_date_created'] = job.date_created
		context_dict['job_due_date'] = job.due_date
		context_dict['job_price'] = job.price

		#expirimental - get comments
		comment_list = job.comment_set.all()
		context_dict['comments'] = comment_list

	except Job.DoesNotExist:
		pass

	return render(request, 'jobs_dash/job_detail.html', context_dict)
