from django.forms.widgets import DateInput


class JQueryUIDateWidget(DateInput):
    def __init__(self, attrs=None, format=None):
        if attrs is None:
            attrs = {}
        attrs['class'] = "datepicker"
        super(JQueryUIDateWidget, self).__init__(attrs, format)
