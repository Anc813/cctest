from django.db.models.signals import post_save, post_delete
from django.db.utils import DatabaseError
from django.contrib.contenttypes.models import ContentType

from .models import SignalProcessor


def object_listener(sender, **kwargs):
    if sender is SignalProcessor or kwargs.get('raw', False):
        return

    action = 'D' if not 'created' in kwargs else 'C' if kwargs[
        'created'] else 'U'

    try:
        ct = ContentType.objects.get_for_model(sender)
        SignalProcessor(app_name=ct.app_label,
                    model_name=ct.model,
                    action=action,
                    object_pk=kwargs['instance'].pk).save()
    except DatabaseError:
        pass
    pass


post_save.connect(object_listener)
post_delete.connect(object_listener)
