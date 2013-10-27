from django.conf.urls import patterns, include, url
from school.views import home,about,achievements,academics,parent,alumni,gallery,activities,facilities
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$',home),
	url(r'^about$',about),
	url(r'^achievements$',achievements),
	url(r'^academics$',academics),
#	url(r'^activities$',activities),
	url(r'^facilities$',facilities),
	url(r'^parent-information$',parent),
	url(r'^alumni$',alumni),
	url(r'^gallery$',gallery),
)
