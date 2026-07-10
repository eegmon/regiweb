from django.shortcuts import render
from django.http import JsonResponse
from .models import Event
import json

def calendar(request):
    return render(request, "calendar.html")


def event_list(request):
    events = Event.objects.all()

    data = []

    for event in events:
        data.append({
            "id": event.id,
            "title": event.title,
            "start": event.start.isoformat(),
            "end": event.end.isoformat(),
            "color": event.color,
        })

    return JsonResponse(data, safe=False)


def add_event(request):
    if request.method == "POST":
        data = json.loads(request.body)

        Event.objects.create(
            title=data["title"],
            start=data["start"],
            end=data["end"],
            color=data.get("color", "#3788d8")
        )

        return JsonResponse({"status": "success"})