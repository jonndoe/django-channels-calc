from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "livecalculator/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add somecontext here
        return context


