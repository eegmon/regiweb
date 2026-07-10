from django.db import models
from django.conf import settings

class GuestbookEntry(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name='guestbook_entries')
    nickname = models.CharField(max_length=30, default='익명')
    # 1. 제목 필드 추가 (최대 100자)
    title = models.CharField(max_length=100, default='제목 없음') 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.title}] {self.nickname} - {self.created_at:%Y-%m-%d %H:%M}'