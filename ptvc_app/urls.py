from django.urls import path, re_path
from ptvc_app import views


app_name = 'ptvc_app'
urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^about/$', views.AboutView.as_view(), name='about'),
    re_path(r'^bishop/$', views.ProductBishopView.as_view(), name='product_bishop'),
    re_path(r'^under-construction/$', views.UnderConstructionView.as_view(), name='under_construction'),
    re_path(r'^contact/$', views.ContactView.as_view(), name='contact'),
    re_path(r'^product-headline/$', views.ProductHeadlineView.as_view(), name='product_headline'),
    re_path(r'^faq/$', views.FaqView.as_view(), name='faq'),
    re_path(r'^your-questions/$', views.QuestionView.as_view(), name='question_list'),
    re_path(r'^your-questions/new-question/$', views.AddQuestionView.as_view(), name='new_question'),
]
