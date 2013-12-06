from django import template
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType

register = template.Library()


@register.simple_tag
def edit_link(element):
    """
    https://docs.djangoproject.com/en/1.6/ref/contrib/admin/#reversing-admin-urls
    """
    ct = ContentType.objects.get_for_model(element.__class__)
    return reverse("admin:%s_%s_change" % (ct.app_label, ct.model), args=(element.id,))
