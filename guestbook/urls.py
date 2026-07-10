from django.urls import path
from guestbook import views as guestbook_views

# urls.py 파일에서 방명록 부분을 찾아 아래처럼 수정합니다.
urlpatterns = [
    # ... 기존 다른 앱 주소들 (admin, accounts 등) ...

    # 기존 'guestbook/ guestbook/guestbook/' 부분을 아래와 같이 변경합니다.
    path('guestbook/', guestbook_views.guestbook_view, name='guestbook'),
    
    # 글쓰기 페이지 경로를 확실하게 매칭합니다.
    path('guestbook/write/', guestbook_views.guestbook_write, name='guestbook_write'),

    # ... 나머지 주소들 ...
]