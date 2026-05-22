from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_value(): # 입력한 값이 유효하다면
            # 실제 회원 데이터베이스에 저장
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            return redirect('login') # 가입 성공 시 로그인 페이지로 이동 (나중에 구현)
    else:
        form = SignUpForm() # 빈 가입 양식 보여주기
        
    return render(request, 'register/register.html', {'form': form})

# Create your views here.
