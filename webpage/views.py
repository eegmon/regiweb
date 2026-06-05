from django.shortcuts import render

# Create your views here.

def minigame_view(request):
    return render(request, 'minigame/minigame.html')