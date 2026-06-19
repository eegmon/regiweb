from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from .models import GalleryPost


def gallery_page(request):
	return render(request, 'gallery/gallery.html')


@require_GET
def post_list_api(request):
	posts = GalleryPost.objects.all()

	data = [
		{
			'id': post.id,
			'imgUrl': post.image.url,
			'content': post.content,
			'tags': [tag for tag in post.tags.split() if tag],
		}
		for post in posts
	]

	return JsonResponse({'posts': data})


@require_POST
def post_create_api(request):
	image = request.FILES.get('image')
	content = request.POST.get('content', '').strip()
	raw_tags = request.POST.get('tags', '').strip().split()

	if image is None:
		return JsonResponse({'error': '사진을 선택해주세요.'}, status=400)

	processed_tags = []
	for tag in raw_tags:
		if not tag:
			continue
		processed_tags.append(tag if tag.startswith('#') else f'#{tag}')

	post = GalleryPost.objects.create(
		image=image,
		content=content,
		tags=' '.join(processed_tags),
	)

	return JsonResponse(
		{
			'id': post.id,
			'imgUrl': post.image.url,
			'content': post.content,
			'tags': processed_tags,
		},
		status=201,
	)
