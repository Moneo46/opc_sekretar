from django.shortcuts import render

def create_record(request):
	return render(request, 'database/create_record.html', {})