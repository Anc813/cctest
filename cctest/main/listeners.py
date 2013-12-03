from django.db.models.signals import post_save, post_delete
from .models import SignalProcessor
from django.db.utils import OperationalError

def object_listener(sender, **kwargs):
    if sender is SignalProcessor or kwargs.get('raw', False):
        return

    action = 'D' if not 'created' in kwargs else 'C' if kwargs['created'] else 'U'

    try:
        SignalProcessor(app_name = sender._meta.app_label,
                    model_name = sender._meta.model_name,
                    action = action,
                    object_pk = kwargs['instance'].pk
                    ).save()
    except OperationalError:
        pass

post_save.connect(object_listener)
post_delete.connect(object_listener)