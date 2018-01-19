from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^contact/', include('contact.urls')),
	url(r'^services/$', views.services, name='services'),
	url(r'^resources/$', views.resources, name='resources')
]