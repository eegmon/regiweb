from django.urls import path
from guestbook import views as guestbook_views

# urls.py 파일에서 방명록 부분을 찾아 아래처럼 수정합니다.
urlpatterns = [
    # ... 기존 다른 앱 주소들 (admin, accounts 등) ...

    # Include'd under /guestbook/ in project urls, so use '' and 'write/' here.
    path('', guestbook_views.guestbook_view, name='guestbook'),
    path('write/', guestbook_views.guestbook_write, name='guestbook_write'),

    # ... 나머지 주소들 ...
]