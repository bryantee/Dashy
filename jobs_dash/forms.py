from django import forms
from jobs_dash.models import Job, Comment, Issue

class CommentForm(forms.ModelForm):
	#date = forms.DateTimeField(widget=forms.HiddenInput())
	#text = forms.TextInput()
	#job = forms.


	class Meta:
		model = Comment
		fields = ('job', 'text',)

	

