from django.db import models


class PopupNotice(models.Model):
	title = models.CharField(max_length=200)
	image_url = models.URLField(blank=True)
	content = models.TextField()
	is_active = models.BooleanField(default=True)
	starts_at = models.DateTimeField(null=True, blank=True)
	ends_at = models.DateTimeField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Event(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	start = models.DateTimeField()
	end = models.DateTimeField()
	color = models.CharField(max_length=20, default="#3788d8")

	class Meta:
		ordering = ["start", "end"]

	def __str__(self):
		return self.title
