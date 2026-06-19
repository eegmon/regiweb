from django.db import models

class GalleryPost(models.Model):
	image = models.FileField(upload_to='gallery_posts/')
	content = models.TextField(blank=True)
	tags = models.CharField(max_length=500, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return f'GalleryPost({self.id})'
