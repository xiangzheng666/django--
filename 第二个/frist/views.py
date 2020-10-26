from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from . import models
# Create your views here.

def f1(request):
	html=get_template("test.html")
	return HttpResponse(html.render())

def f2(request):
	html=get_template("test.html")
	name=request.GET["name"]
	number=request.GET["number"]
	address=request.GET["address"]
	if name!='' and number!='' and address!='':

		tcpg = models.my_data(name=name,number=number,address=address)
		tcpg.save()

		rs = models.my_data.objects.all()
		models.my_data.objects.filter(name='').delete()
		
		return HttpResponse(html.render({'f':rs}))
	else:
		rs = models.my_data.objects.all()
		models.my_data.objects.filter(name='').delete()
		return HttpResponse(html.render({'f':rs}))