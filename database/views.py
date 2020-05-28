from django.shortcuts import render
from .models import Registry
from django.utils import timezone

def create_record(request):
	rows = Registry.objects.filter(date_created__lte=timezone.now()).order_by('date_created')
	return render(request, 'database/create_record.html', {'rows':rows})