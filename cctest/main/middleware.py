from .models import HTTPRequest


def serialize_value(value):
    from django.contrib.sessions.backends.db import SessionStore

    if isinstance(value, (str, unicode)):
        return value
    elif isinstance(value, (dict, SessionStore)):
        result = []
        for name, val in value.items():
            result.append('%s = %s' % (name, val))
        return '\n'.join(result)
    elif value is None:
        return ''
    else:
        return 'Unknown'


class StoreRequestsDB(object):
    def process_request(self, request):

        if request.user.is_authenticated():
            user = request.user
        else:
            user = None

        HTTPRequest(
            path=serialize_value(request.path),
            path_info=serialize_value(request.path_info),
            method=serialize_value(request.method),
            encoding=serialize_value(request.encoding),
            GET=serialize_value(request.GET),
            POST=serialize_value(request.POST),
            COOKIES=serialize_value(request.COOKIES),
            FILES=serialize_value(request.FILES),
            META=serialize_value(request.META),
            user=user,
            session=serialize_value(request.session)
        ).save()
