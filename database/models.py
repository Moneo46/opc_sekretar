from django.db import models
from django.conf import settings
from django.utils import timezone


class Registry(models.Model):

	fio = models.CharField(max_length=255)
	mail_response=models.CharField(max_length=255,blank=True,null=True)
	priem_data=models.DateField(auto_now=False,auto_now_add=False)
	priem_fio=models.CharField(max_length=255)
	priem_doljnost=models.CharField(max_length=255)
	priem_content=models.TextField(blank=True, null=True)
	priem_results=models.TextField(blank=True,null=True)

	destination=models.CharField(max_length=255,blank=True,null=True)
	data_prinytiy=models.DateField(auto_now=False,auto_now_add=False)
	number=models.IntegerField()
	created_fio=models.CharField(max_length=255)
	created_doljnost=models.CharField(max_length=255)
	comment=models.TextField(blank=True,null=True)
	date_created=models.DateTimeField(auto_now=True)

	def recording(self):
		self.date_created=timezone.now()
		self.save()

	def __str__(self):
		return self.fio