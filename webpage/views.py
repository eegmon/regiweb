from django.shortcuts import render

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
    return render(request, 'main/main.html')