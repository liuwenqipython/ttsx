from django.conf.urls import url
import views

urlpatterns = [
    url(r'^register/$',views.register),
    url(r'^register_cheak/$',views.register_cheak),
    url(r'^register_verify/$',views.register_verify),
    url(r'^login/$',views.login),
    url(r'^login_cheak/$',views.login_cheak),
    #url(r'^index/$',views.index),
    url(r'^info/$',views.info),
    url(r'^order/$',views.order),
    url(r'^site/$',views.site),
    url(r'^site_cheak/$',views.site_cheak),
    url(r'^login_stop/$',views.login_stop),

]