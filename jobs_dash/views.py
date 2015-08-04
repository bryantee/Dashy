from django.shortcuts import render
from django.http import HttpResponse
from jobs_dash.models import Job
from datetime import datetime
from jobs_dash.forms import CommentForm, JobForm
from django.http import HttpResponseRedirect


def index(request):
	jobs_list = Job.objects.order_by('due_date')
	jobs_open_list = [j for j in jobs_list if j.is_open]
	context_dict = {'open_jobs': jobs_open_list}

	def was_invoiced_10_days_ago(job):
		if job.invoiced_date:
			today = datetime.today().date()
			dt = today - job.invoiced_date
			print(dt.total_seconds())
			if dt.total_seconds() <= 864000:
				return True
			else:
				return False

	# get total open invoicables
	total_open_money = 0
	for j in jobs_open_list:
		if j.is_invoiced == False:
			total_open_money += j.price
	context_dict['open_money'] = total_open_money

	# get total jobs that have been invoiced
	total_invoiced = 0
	invoiced_jobs = [j for j in jobs_list if j.is_invoiced]
	invoiced_last_10 = [j for j in invoiced_jobs if was_invoiced_10_days_ago(j)]

	print invoiced_last_10
	for j in invoiced_last_10:
			total_invoiced += j.price
	context_dict['invoiced'] = total_invoiced
	context_dict['invoiced_jobs'] = invoiced_last_10

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
	context_dict['job_status'] = job.is_open

	#expirimental - get comments
	comment_list = job.comment_set.all().order_by('date')
	context_dict['comments'] = comment_list

	# Show current issues
	# Future plans for link to more details on issues and past issues
	issues_list = job.issue_set.all()
	issues_count = len(issues_list)
	issues_list_open = [i for i in issues_list if i.is_open]
	open_issues_count = len(issues_list_open)
	context_dict['issues_count'] = issues_count
	context_dict['issues_list'] = issues_list
	context_dict['open_issues_count'] = open_issues_count


	# Calculates days left until project due	
	today = datetime.today().date()
	dt = job.due_date - today
	context_dict['dt'] = dt

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return HttpResponseRedirect('/jobs/%s/' % job_address_slug)
		else:
			print form.errors
	else:
		form = CommentForm(initial={'job': job.id})

	context_dict['form'] = form
	context_dict['slug'] = job_address_slug
	context_dict['job'] = job

######################
### Testing below ####
######################

	# Testing for initial
	print form['job'].value()
	# Testing for img url
	print(job.pic.url)

######################
### End Test #########
######################

	return render(request, 'jobs_dash/job_detail.html', context_dict)

def add_job(request):

	if request.method == 'POST':
		form = JobForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return HttpResponseRedirect('/jobs/')
		else:
			print form.errors
	else:
		form = JobForm()

	return render(request, 'jobs_dash/add_job.html', {'form': form})
