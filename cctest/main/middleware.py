from .models import HTTPRequest


def serializeValue(value):
    if isinstance(value, (str, unicode)):
        return value
    elif isinstance(value, dict):
        result = []
        for name, val in value.items():
            result.append('%s = %s' %(name, val))
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
            body = serializeValue(request.body),
            path = serializeValue(request.path),
            path_info = serializeValue(request.path_info),
            method = serializeValue(request.method),
            encoding = serializeValue(request.encoding),
            GET = serializeValue(request.GET),
            POST = serializeValue(request.POST),
            COOKIES = serializeValue(request.COOKIES),
            FILES = serializeValue(request.FILES),
            META = serializeValue(request.META),
            user = user,
            session = serializeValue(request.body)


        ).save()