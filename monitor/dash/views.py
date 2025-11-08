from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Endpoints, TrafficLog


def index(request):
    endpoint_list = Endpoints.objects.order_by('ip_address')
    output = {'endpoint_list': endpoint_list}
    return render(request, "dash/index.html", output)

def endpoints(request):
    return HttpResponse("Hello, world - endpoints.")

def traffic(request):
    return HttpResponse("Hello, world - traffic.")

def detail(request, ip_address):
    endpoint = get_object_or_404(Endpoints, pk=ip_address)
    traffic = TrafficLog.objects.filter(ip_src=endpoint.ip_address).order_by('-interval_start')
    return render(request, "dash/detail.html", {'endpoint': endpoint, 'traffic': traffic})
