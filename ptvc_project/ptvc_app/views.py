from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'ptvc_app/index.html'


class AboutView(TemplateView):
    template_name = 'ptvc_app/aboutus.html'


class PricingView(TemplateView):
    template_name = 'ptvc_app/product_pricing.html'
