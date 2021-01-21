from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Coordinates


def index(request):
    all_entries = Coordinates.objects.all()
    return render(request, "map/index.html", context={
        "title": "Sarah's Map", "all_entries": all_entries
    })

def create_point(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    latitude = body["latitude"]
    longitude = body["longitude"]
    Coordinates.objects.create(x=latitude, y=longitude)
    return HttpResponse(status=200)

# Create your views here.
