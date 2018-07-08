from django.shortcuts import render
from django.http import HttpResponse
from .models import Page
import string
import random
import time

def write(request):
	page = Page(title=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)))
	page.save()

	return HttpResponse(page.title)

def read(request):
	page = Page.objects.order_by('?').first()

	return HttpResponse(page.title)

def sleep(request):
	time.sleep(1)

	return HttpResponse('sleeped')
