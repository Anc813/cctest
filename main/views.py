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
    sort_fields = ('timestamp', 'priority')

    def get_sort_order(self):
        order = self.request.GET.get('sort', '')
        if order:
            is_desc = '-' if order[0] == '-' else ''
            order = order[1:] if order[0] == '-' else order
            if order in self.model._meta.get_all_field_names():
                return order, is_desc
        return '', True


    def get_queryset(self):
        order_field, is_desc = self.get_sort_order()
        if order_field:
            if is_desc:
                order_field = '-' + order_field
            return HTTPRequest.objects.all().order_by(order_field)[:10]
        else:
            return HTTPRequest.objects.all()[:10]

    def get_context_data(self, **kwargs):
        context = super(HTTPRequestView, self).get_context_data(**kwargs)

        context['sort'] = {}
        ctx = context['sort']
        order_field, is_desc = self.get_sort_order()
        for field in self.sort_fields:
            ctx[field] = {}
            order = '-'
            if field == order_field:
                order = '' if is_desc else '-'
                ctx[field]['class'] = 'desc-sort' if is_desc else 'asc-sort'
            ctx[field]['href'] = '?sort=%s%s' % (order, field)

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
