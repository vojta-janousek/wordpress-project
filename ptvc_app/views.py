from django.views.generic import TemplateView

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


class AskView(TemplateView):
    template_name = 'ptvc_app/ask.html'


class ProductHeadlineView(TemplateView):
    template_name = 'ptvc_app/product_headline.html'
