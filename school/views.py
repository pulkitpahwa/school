from django.http import HttpResponse
from django.template import Context,Template
from django.template.loader import get_template
from django.shortcuts import render
from django.views.generic import CreateView
from coke.models import Notice

def gallery(request) :
	a = get_template("gallery.html")
	w = Notice.objects.all()
	c =Context({'title':"sitemap",'w':w})
	html = a.render(c)
	return HttpResponse(html)

def home(request) :
	a = get_template("index.html")
	w = Notice.objects.all()
	c =Context({'title':"sitemap",'w':w})
	html = a.render(c)
	return HttpResponse(html)


def gallery(request) :
	a = get_template("gallery.html")
	w = Notice.objects.all()
	c =Context({'title':"sitemap",'w':w})
	html = a.render(c)
	return HttpResponse(html)

def alumni(request) :
	a = get_template("alumni.html")
	w = Notice.objects.all()
	c =Context({'title':"sitemap",'w':w})
	html = a.render(c)
	return HttpResponse(html)


def about(request) :
	a = get_template("about.html")
	w = Notice.objects.all()
	c =Context({'title':"sitemap",'w':w})
	html = a.render(c)
	return HttpResponse(html)

def parent(request) :
	a = get_template("parent.html")
	w = Notice.objects.all()
	c =Context({'title':"sitemap",'w':w})
	html = a.render(c)
	return HttpResponse(html)

def academics(request) :
	a = get_template("academics.html")
	w = Notice.objects.all()
	c =Context({'title':"sitemap",'w':w})
	html = a.render(c)
	return HttpResponse(html)

def achievements(request) :
	a = get_template("alumni.html")
	w = Notice.objects.all()
	c =Context({'title':"sitemap",'w':w})
	html = a.render(c)
	return HttpResponse(html)


def activities(request) :
	a = get_template("activities.html")
	w = Notice.objects.all()
	c =Context({'title':"sitemap",'w':w})
	html = a.render(c)
	return HttpResponse(html)


def facilities(request) :
	a = get_template("facilities.html")
	w = Notice.objects.all()
	c =Context({'title':"sitemap",'w':w})
	html = a.render(c)
	return HttpResponse(html)

