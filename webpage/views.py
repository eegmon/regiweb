from django.db.models import Q
from django.shortcuts import render
from django.utils import timezone

from .models import PopupNotice

# Create your views here.
def privacy_policy_view(request):
    return render(request, 'privacy_policy/privacy_policy.html')

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