from django.urls import path, re_path
from ptvc_app import views


app_name = 'ptvc_app'
urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^about/$', views.AboutView.as_view(), name='about'),
    re_path(r'^pricing/$', views.PricingView.as_view(), name='pricing'),
]
