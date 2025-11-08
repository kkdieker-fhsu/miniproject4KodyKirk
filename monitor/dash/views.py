from django.http import HttpResponse

from monitor.dash.models import Endpoints


def index(request):
    endpoint_list = Endpoints.objects.order_by('ip_address')
    output = ", ".joing([e.ip_address for e in endpoint_list])
    return HttpResponse(output)


