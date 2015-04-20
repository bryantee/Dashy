from django import forms
from jobs_dash.models import Job, Comment, Issue

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('job', 'text')
		widgets = {'job': forms.HiddenInput(),}