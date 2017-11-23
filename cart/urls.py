from django.conf.urls import include, url
from .import views

urlpatterns = [
	url(r'^$',views.add_to_cart),
	url(r'^delete/',views.delete_from_cart),
]