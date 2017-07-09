from django.conf.urls import url
import views
urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^goodslist/$',views.goodslist),
    url(r'^detail/$',views.detail),
]
