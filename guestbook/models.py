from django.db import models
from django.conf import settings

class GuestbookEntry(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name='guestbook_entries')
	nickname = models.CharField(max_length=30, default='익명')
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.nickname} - {self.created_at:%Y-%m-%d %H:%M}'
