from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    # 비밀번호 입력창과 비밀번호 확인창을 만듭니다.
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호")
    password_check = forms.CharField(widget=forms.PasswordInput, label="비밀번호 확인")

    class Meta:
        model = User
        fields = ['username', 'email'] # 아이디와 이메일만 입력받음

    # 두 비밀번호가 일치하는지 검사하는 서브 함수
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_check = cleaned_data.get("password_check")

        if password != password_check:
            self.add_error('password_check', "비밀번호가 일치하지 않습니다.")