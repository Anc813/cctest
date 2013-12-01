from django.views.generic import DetailView, ListView, UpdateView
from .models import People, HTTPRequest
from .widgets import JQueryUIDateWidget
from django.forms.models import modelform_factory
# Create your views here.

class HomeView(DetailView):
    model = People
    template_name = "main/home.html"

class HTTPRequestView(ListView):
    model = HTTPRequest
    template_name = "main/requests.html"

    def get_queryset(self):
        return HTTPRequest.objects.all()[:10]

class HomeEditView(UpdateView):
    model = People
    form_class =  modelform_factory(People, widgets={"birth_date": JQueryUIDateWidget })

    def dispatch(self, request, *args, **kwargs):
        self.template_name = "main/edit_form.html" if self.request.is_ajax() else "main/edit.html"
        return super(HomeEditView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        from django.http import HttpResponseRedirect

        self.object = form.save()

        if self.request.is_ajax():
            return self.render_to_response(self.get_context_data(form=form, success="Changes have been saved"))
        else:
            return HttpResponseRedirect(self.get_success_url())