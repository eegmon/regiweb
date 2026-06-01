from django.shortcuts import render

# Create your views here.
def privacy_policy_view(request):
    return render(request, 'privacy_policy/privacy_policy.html')