from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import GuestbookEntry

# 1. 방명록 목록 및 수정/삭제만 담당 (글 생성 코드는 여기서 완전히 제거됨)
def guestbook_view(request):
    if request.method == 'POST':
        action = request.POST.get('action', '')

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

        # ⚠️ 중요: 기존 코드 맨 아래에 있던 nickname, content 처리 및 GuestbookEntry.objects.create 로직을 여기서 완전히 지워야 합니다.

    # GET 요청 시 목록만 보여줌
    entries = GuestbookEntry.objects.order_by('-created_at')
    return render(request, 'guestbook.html', {'entries': entries})


# 2. 독립된 새 글 작성 페이지 및 저장만 담당
def guestbook_write(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        
        nickname = '익명'
        if request.user.is_authenticated:
            nickname = request.user.username

        if title and content:
            GuestbookEntry.objects.create(
                author=request.user if request.user.is_authenticated else None,
                nickname=nickname,
                title=title,       # 새로운 제목 필드
                content=content,
            )
            return redirect('guestbook') # 저장 후 메인 페이지로 이동

    return render(request, 'write.html')