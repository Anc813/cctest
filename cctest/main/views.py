from django.views.generic import DetailView, ListView, UpdateView
from django.forms.models import modelform_factory

from .models import People, HTTPRequest
from .widgets import JQueryUIDateWidget


class HomeView(DetailView):
    model = People
    template_name = "main/home.html"


class HTTPRequestView(ListView):
    model = HTTPRequest
    template_name = "main/requests.html"

    def get_queryset(self):
        order = self.request.GET.get('sort', '')
        if order and order in self.model._meta.get_all_field_names():
            return HTTPRequest.objects.all().order_by('-' + order)[:10]
        else:
            return HTTPRequest.objects.all()[:10]

    def get_context_data(self, **kwargs):
        context = super(HTTPRequestView, self).get_context_data(**kwargs)
        order = self.request.GET.get('sort', '')
        if order and order in self.model._meta.get_all_field_names():
            context['sort']= {}
            context['sort'][order] = True
        return context

class HomeEditView(UpdateView):
    model = People
    form_class = modelform_factory(People,
                                   widgets={"birth_date": JQueryUIDateWidget})

    def dispatch(self, request, *args, **kwargs):
        self.template_name = "main/edit_form.html" if self.request.is_ajax() \
            else "main/edit.html"
        return super(HomeEditView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        from django.http import HttpResponseRedirect

        self.object = form.save()

        if self.request.is_ajax():
            return self.render_to_response(
                self.get_context_data(form=form,
                                      success="Changes have been saved",
                                      redirect_uri=self.get_success_url()))
        else:
            return HttpResponseRedirect(self.get_success_url())
