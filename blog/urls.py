from django.conf.urls import url
from .views import (
	index,
	create,
	detail,
	delete,
	update,
	)

urlpatterns = [
	url(r'^$', index),
	url(r'^create/$', create),
	url(r'^detail/$', detail),
	url(r'^delete/$', delete),
	url(r'^update/$', update),
]
