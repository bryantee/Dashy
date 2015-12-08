from django.db import models
from django.template.defaultfilters import slugify
from PIL import Image
from datetime import datetime

class Client(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return self.name

class City(models.Model):
	city_name = models.CharField(max_length=30)

	def __unicode__(self):
		return self.city_name

class Job(models.Model):
	client = models.ForeignKey(Client, verbose_name="Client", blank=True, null=True)
	address = models.CharField(max_length=128, unique=True, verbose_name="Address (No City)")
	city = models.ForeignKey(City, verbose_name="City", blank=True, null=True)
	due_date = models.DateField()
	date_created = models.DateField(auto_now_add=True)
	time_created = models.TimeField(auto_now_add=True)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	pic = models.ImageField("House Pic", upload_to="images/", blank=True, null=True)
	purchase_order = models.FileField("Purchase Order", upload_to="pos/", blank=True, null=True)
	repair_po = models.FileField("Repairs PO", upload_to="pos/", blank=True, null=True)
	paint_po = models.FileField("Paint PO", upload_to="pos/", blank=True, null=True)
	slug = models.SlugField(unique=True)
	flooring = models.BooleanField(default=False)
	flooring_date = models.DateField(blank=True, null=True)
	agent_name = models.CharField(max_length=128, blank=True, null=True)
	agent_phone = models.CharField(max_length=12, blank=True, null=True)
	agent_email = models.EmailField(max_length=128, blank=True, null=True)
	is_open = models.BooleanField(default=True)
	is_invoiced = models.BooleanField(default=False)
	invoiced_date = models.DateField(blank=True, null=True)
	invoice_number = models.PositiveIntegerField(blank=True, null=True)
	is_paid = models.BooleanField(default=False)
	paid_date = models.DateField(blank=True, null=True)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.address)
		super(Job, self).save(*args, **kwargs)

	def invoice(self):
		self.invoiced_date = datetime.now
		self.is_invoiced = True
		self.is_open = False
		print("Invoiced!")

	def __unicode__(self):
		return self.address	

class Comment(models.Model):
	job = models.ForeignKey(Job)
	date = models.DateTimeField(auto_now_add=True)
	text = models.TextField(blank=False)

	def __unicode__(self):
		return str(self.job) + ' - ' + str(self.date)

class Issue(models.Model):
	job = models.ForeignKey(Job)
	date = models.DateTimeField(auto_now_add=True)
	text = models.CharField(max_length=128)

	# Used to distinguish between issues that have been solved
	# True means the issue is still open and needs attention
	is_open = models.BooleanField(default=True)

	def __unicode__(self):
		return  str(self.job) + ' - ' + str(self.date)


