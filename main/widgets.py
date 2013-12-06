from django.forms.widgets import DateInput
from django.conf import settings
from django.utils.safestring import mark_safe

class JQueryUIDateWidget(DateInput):
    class Media:
        css = {
            'all': (settings.STATIC_URL+"css/jquery-ui.css",)
        }
        js = (
            settings.STATIC_URL+"js/jquery.min.js",
            settings.STATIC_URL+"js/jquery-ui.min.js",
        )

    def __init__(self, attrs=None, format=None):
        if attrs is None:
            attrs = {}
        if 'class' in attrs:
            attrs['class'] += " datepicker"
        else:
            attrs['class'] = "datepicker"

        super(JQueryUIDateWidget, self).__init__(attrs, format)

    def render(self, name, value, attrs=None):
        return super(JQueryUIDateWidget, self).render(name, value, attrs) + \
            mark_safe('<script>jQuery(".datepicker").datepicker();</script>')

