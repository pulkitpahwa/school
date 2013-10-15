from django.http import HttpResponse
from django.template import Context,Template
from django.template.loader import get_template
from django.shortcuts import render
from django.views.generic import CreateView
from management.models import Holidays,Prospective_student,current_student, Event,Exam_rule

def gallery(request) :
	a = get_template("gallery.html")
	c =Context({'title':"sitemap"})
	html = a.render(c)
	return HttpResponse(html)

def home(request) :
	a = get_template("index.html")
	c =Context({'title':"sitemap"})
	html = a.render(c)
	return HttpResponse(html)


def gallery(request) :
	a = get_template("gallery.html")
	c =Context({'title':"sitemap"})
	html = a.render(c)
	return HttpResponse(html)

def alumni(request) :
	a = get_template("alumni.html")
	c =Context({'title':"sitemap"})
	html = a.render(c)
	return HttpResponse(html)


def about(request) :
	a = get_template("about.html")
	c =Context({'title':"sitemap"})
	html = a.render(c)
	return HttpResponse(html)

def parent(request) :
	a = get_template("parent.html")
	c =Context({'title':"sitemap"})
	html = a.render(c)
	return HttpResponse(html)

def academics(request) :
	a = get_template("academics.html")
	c =Context({'title':"sitemap"})
	html = a.render(c)
	return HttpResponse(html)

def achievements(request) :
	a = get_template("alumni.html")
	c =Context({'title':"sitemap"})
	html = a.render(c)
	return HttpResponse(html)


def activities(request) :
	a = get_template("activities.html")
	c =Context({'title':"sitemap"})
	html = a.render(c)
	return HttpResponse(html)


def facilities(request) :
	a = get_template("facilities.html")
	c =Context({'title':"sitemap"})
	html = a.render(c)
	return HttpResponse(html)

