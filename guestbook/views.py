from django.shortcuts import render

# Create your views here.
def guestbook_view(request):
    return render(request, 'guestbook.html')