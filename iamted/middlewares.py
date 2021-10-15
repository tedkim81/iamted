from django.http import HttpResponse

class CommonMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.GET.get('error_status', None):
            return HttpResponse(status=request.GET.get('error_status'))
        return self.get_response(request)