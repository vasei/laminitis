# djangotemplates/example/views.py
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView  # Import TemplateView


# Add the two views we have been talking about  all this time :)
@method_decorator(login_required, name='dispatch')
class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
