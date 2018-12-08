from django.http import HttpResponse
from django.views import View


class RatingView(View):
    def get(self, request):
        html = '<h1>How do we do?</h1>'
        return HttpResponse(html)
