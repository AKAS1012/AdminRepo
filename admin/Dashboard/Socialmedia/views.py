from django.views.generic import TemplateView


class Dashboard(TemplateView):
    template_name = 'dashboard/dashboard_form.html'

class Home(TemplateView):
    template_name = 'dashboard/add_home.html'

class Update(TemplateView):
    template_name = 'dashboard/updates.html'
