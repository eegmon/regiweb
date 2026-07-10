from django.db.models import Q
from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from .models import Event
import json

from .models import PopupNotice

# Create your views here.
def privacy_policy_view(request):
    return render(request, 'privacy_policy/privacy_policy.html')
def calendar(request):
    return render(request, "calendar.html")

def minigame_view(request):
    return render(request, 'minigame/minigame.html')

def introduce_view(request):
    return render(request, 'introduce/index.html')

def calendar_view(request):
    return render(request, 'calendar/calendar.html')

def main_view(request):
    now = timezone.now()
    popup_notice = (
        PopupNotice.objects.filter(is_active=True)
        .filter(Q(starts_at__isnull=True) | Q(starts_at__lte=now))
        .filter(Q(ends_at__isnull=True) | Q(ends_at__gte=now))
        .first()
    )
    return render(request, 'main/main.html', {'popup_notice': popup_notice})

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