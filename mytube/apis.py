from django.http import JsonResponse
from mytube.libs import youtube

def recommend_words(request):
    # TODO: 일단은 빠른 클라 구현을 위해 하드코딩. 여기에 로직을 심어야 한다.
    return JsonResponse({
        'recommend_words': [
            'NBA', 'MLB', '류현진', '코로나19', '도쿄올림픽', 'LPGA', '에비앙챔피언쉽', '이정은6', '영화 리뷰', '스포츠 하이라이트'
        ]
    })

def search(request):
    max_size = request.GET.get('max_size', 100)
    result = youtube.search(request.GET.get('q', None), max_size)
    return JsonResponse({ 'search_results': result })