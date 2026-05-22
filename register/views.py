from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.urls import reverse

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid(): # 입력한 값이 유효하다면
            # 실제 회원 데이터베이스에 저장
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # 가입 성공 후 GET 요청으로 PRG 패턴을 적용하여 성공 플래그 전달
            return redirect(f"{reverse('signup')}?success=1")
    else:
        form = SignUpForm() # 빈 가입 양식 보여주기

    # 성공 여부를 쿼리 파라미터로 전달받아 템플릿에 노출
    success = request.GET.get('success') == '1'
    return render(request, 'register/register.html', {'form': form, 'success': success})

# Create your views here.
