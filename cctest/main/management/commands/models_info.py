from django.core.management.base import BaseCommand
from django.db.models import get_models
from django.template.defaultfilters import pluralize


class Command(BaseCommand):
    help = 'prints all project models and the count of objects in every model'

    def handle(self, *args, **options):
        models = get_models()

        if len(models) == 0:
            s = "no models found"
            self.stdout.write(s)
            self.stderr.write(s)

        for model in models:
            count = model.objects.all().count()
            s = "model %s.%s has %d object%s" % (model._meta.app_label,
                                                 model._meta.model_name, count,
                                                 pluralize(count))
            self.stdout.write(s)
            self.stderr.write('error: %s' % s)
