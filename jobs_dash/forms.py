from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget
from jobs_dash.models import Job, Comment, Issue

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('job', 'text')
		widgets = {'job': forms.HiddenInput(),}

class JobForm(forms.ModelForm):
	class Meta:
		model = Job
		fields = ('address', 'due_date', 'price')
		widgets = {'due_date': SelectDateWidget}