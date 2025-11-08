from django.http import HttpResponse

from dash.models import Endpoints


def index(request):
    endpoint_list = Endpoints.objects.order_by('ip_address')
    output = ", ".join([e.ip_address for e in endpoint_list])
    return HttpResponse(output)
    #return HttpResponse("Hello, world.")

def endpoints(request):
    return HttpResponse("Hello, world - endpoints.")

def traffic(request):
    return HttpResponse("Hello, world - traffic.")

def detail(request, ip_address):
    return HttpResponse(f"Hello, world - detail for {ip_address}.")