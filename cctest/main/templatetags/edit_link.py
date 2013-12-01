from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def edit_link(element):
    '''
    https://docs.djangoproject.com/en/1.6/ref/contrib/admin/#reversing-admin-urls
    '''
    return reverse("admin:%s_%s_change" % (element._meta.app_label, element._meta.model_name), args=(element.id,))