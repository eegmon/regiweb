from django.contrib import admin
from .models import Event

from .models import PopupNotice


@admin.register(PopupNotice)
class PopupNoticeAdmin(admin.ModelAdmin):
	list_display = ('title', 'is_active', 'starts_at', 'ends_at', 'updated_at')
	list_filter = ('is_active',)
	search_fields = ('title', 'content', 'image_url')
	ordering = ('-updated_at',)
