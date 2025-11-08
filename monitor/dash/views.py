from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Endpoints, TrafficLog


def index(request):
    return render(request, "dash/index.html")

def endpoints(request):
    endpoint_list = Endpoints.objects.order_by('ip_address')
    output = {'endpoint_list': endpoint_list}
    return render(request, "dash/endpoints.html", output)

def traffic(request):
    return HttpResponse("Hello, world - traffic.")

def detail(request, ip_address):
    endpoint = get_object_or_404(Endpoints, pk=ip_address)
    traffic = get_list_or_404(TrafficLog, ip_src=endpoint)
    return render(request, "dash/detail.html", {'endpoint': endpoint, 'traffic': traffic})

def external_connections(request):
    return render(request, "dash/external.html")

def endpoint_register(request):
    return render(request, "dash/endpoint_register.html")

def endpoint_submission(request):
    return HttpResponseRedirect(reverse("dash:endpoints"))

