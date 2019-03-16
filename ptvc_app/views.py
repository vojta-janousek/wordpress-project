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
