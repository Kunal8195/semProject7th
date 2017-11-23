from django.conf.urls import url
from .import views

app_name='products'
urlpatterns = [
    url(r'^$', views.products,name='product'),
    #url(r'^product/$',views.product,name='product'),
    #url(r'^product_info/$',views.product_info,name='product_info'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^checkout/$',views.checkout,name='checkout'),
    url(r'^product_info/(?P<product_id>[0-9]+)/$',views.product_info,name='product_info'),     
]
