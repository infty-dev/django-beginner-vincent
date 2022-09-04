from django.views.generic import TemplateView


class HomePagesView(TemplateView):
    template_name: str = "home.html"


class AboutPagesView(TemplateView):
    template_name: str = "about.html"
