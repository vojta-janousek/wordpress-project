from django.views.generic import TemplateView, ListView, CreateView
from django.contrib import messages

from ptvc_app.models import Contact
from ptvc_app.forms import AddQuestionForm

# Create your views here.
class IndexView(TemplateView):
    template_name = 'ptvc_app/index.html'


class AboutView(TemplateView):
    template_name = 'ptvc_app/aboutus.html'


class ProductBishopView(TemplateView):
    template_name = 'ptvc_app/product_bishop.html'


class UnderConstructionView(TemplateView):
    template_name = 'ptvc_app/under_construction.html'


class ContactView(TemplateView):
    template_name = 'ptvc_app/contact.html'


class FaqView(TemplateView):
    template_name = 'ptvc_app/faq.html'


class ProductHeadlineView(TemplateView):
    template_name = 'ptvc_app/product_headline.html'


class QuestionView(ListView):
    template_name = 'ptvc_app/question_list.html'
    queryset = Contact.objects.exclude(answer="")


class AddQuestionView(CreateView):
    redirect_field_name = 'ptvc_app/question_list.html'
    form_class = AddQuestionForm
    model = Contact


class HelpdeskView(TemplateView):
    template_name = 'ptvc_app/helpdesk.html'

# -----------------------------------------------
