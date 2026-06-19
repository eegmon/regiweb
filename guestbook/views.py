from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import GuestbookEntry

def guestbook_view(request):
    if request.method == 'POST':
        action = request.POST.get('action', 'create')

        if action == 'delete':
            entry_id = request.POST.get('entry_id')
            entry = get_object_or_404(GuestbookEntry, pk=entry_id)

            if entry.author_id == request.user.id or request.user.is_staff:
                entry.delete()

            return redirect('guestbook')

        if action == 'edit':
            entry_id = request.POST.get('entry_id')
            content = request.POST.get('content', '').strip()
            entry = get_object_or_404(GuestbookEntry, pk=entry_id)

            if content and (entry.author_id == request.user.id or request.user.is_staff):
                entry.content = content
                entry.save(update_fields=['content', 'updated_at'])

            return redirect('guestbook')

        nickname = request.POST.get('nickname', '').strip() or '익명'
        content = request.POST.get('content', '').strip()

        if request.user.is_authenticated:
            nickname = request.user.username or nickname

        if content:
            GuestbookEntry.objects.create(
                author=request.user if request.user.is_authenticated else None,
                nickname=nickname,
                content=content,
            )
            return redirect('guestbook')

    entries = GuestbookEntry.objects.order_by('-created_at')
    return render(request, 'guestbook.html', {'entries': entries})