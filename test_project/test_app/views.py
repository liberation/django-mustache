from django.views.generic import TemplateView


class TestView(TemplateView):
    template_name = 'foo_bar.mustache'

    def get_context_data(self):
        return {'foo': u"bar"}
