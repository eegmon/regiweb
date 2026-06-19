from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.urls import reverse


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # PRG 패턴: 성공 시 같은 signup 페이지로 리다이렉트하여 GET 쿼리로 성공 표시
            return redirect(f"{reverse('signup')}?success=1")
    else:
        form = SignUpForm()

    success = request.GET.get('success') == '1'
    return render(request, 'register/register.html', {'form': form, 'success': success})

# Create your views here.
