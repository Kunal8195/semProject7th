from django.conf.urls import url
from . import views
app_name = 'header'

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^login',views.login,name='login'), 
    url(r'^language/(?P<language>[a-z\-]+)/$',views.language),
    url(r'^accounts/login/$',views.login),
    url(r'^accounts/auth/$',views.auth_view,name='auth'),
    url(r'^accounts/logout/$',views.logout,name='logout'),
    url(r'^accounts/loggedin/$',views.loggedin),
    url(r'^accounts/invalid/$',views.invalid_login), 
    url(r'^accounts/register/$',views.register_user),
    url(r'^accounts/register_success/$',views.register_success),
    url(r'^create/$',views.create),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^search/$',views.search)
]
