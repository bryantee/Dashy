from django.db import models
from django.template.defaultfilters import slugify

class Job(models.Model):
	address = models.CharField(max_length=128, unique=True)
	due_date = models.DateField()
	date_created = models.DateField(auto_now_add=True)
	time_created = models.TimeField(auto_now_add=True)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	slug = models.SlugField(unique=True)
	#status = models.BooleanField()
	
	def save(self, *args, **kwargs):
                self.slug = slugify(self.address)
                super(Job, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.address	

class Comment(models.Model):
	job = models.ForeignKey(Job)
	date = models.DateTimeField(auto_now_add=True)
	text = models.TextField(blank=False)

	def __unicode__(self):
		return str(self.date)

class Issue(models.Model):
	job = models.ForeignKey(Job)
	date = models.DateTimeField(auto_now_add=True)
	text = models.CharField(max_length=128)

	# Used to distinguish between issues that have been solved
	# True means the issue is still open and needs attention
	is_open = models.BooleanField(default=True)

	def __unicode__(self):
		return str(self.date)