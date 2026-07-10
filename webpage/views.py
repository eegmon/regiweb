from django.db.models import Q
from django.shortcuts import render
from django.utils import timezone
from django.utils.dateparse import parse_datetime
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
    if request.method != "POST":
        return JsonResponse({"status": "error", "error": "POST required"}, status=405)

    # require authenticated user
    if not request.user or not request.user.is_authenticated:
        return JsonResponse({"status": "error", "error": "authentication required"}, status=401)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"status": "error", "error": "invalid json"}, status=400)

    title = data.get("title")
    if not title or not title.strip():
        return JsonResponse({"status": "error", "error": "title required"}, status=400)

    start_raw = data.get("start")
    end_raw = data.get("end")

    if not start_raw:
        return JsonResponse({"status": "error", "error": "start required"}, status=400)

    start_dt = parse_datetime(start_raw)
    end_dt = parse_datetime(end_raw) if end_raw else None

    if start_dt is None:
        return JsonResponse({"status": "error", "error": "invalid start datetime"}, status=400)
    if end_raw and end_dt is None:
        return JsonResponse({"status": "error", "error": "invalid end datetime"}, status=400)

    # make timezone-aware if naive
    if timezone.is_naive(start_dt):
        start_dt = timezone.make_aware(start_dt, timezone.get_current_timezone())
    if end_dt and timezone.is_naive(end_dt):
        end_dt = timezone.make_aware(end_dt, timezone.get_current_timezone())

    if end_dt and end_dt < start_dt:
        return JsonResponse({"status": "error", "error": "end before start"}, status=400)

    color = data.get("color", "#3788d8")

    event = Event.objects.create(
        title=title.strip(),
        start=start_dt,
        end=end_dt,
        color=color,
    )

    return JsonResponse({"status": "success", "id": event.id})