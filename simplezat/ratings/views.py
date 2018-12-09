from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView


class RatingView(TemplateView):
    template = 'ratings.html'

    def get(self, request):
        return render(
            request,
            self.template
        )


class CommentView(TemplateView):
    template = 'comments.html'

    def get(self, request, rating):
        return render(
            request,
            self.template,
            {'rating': rating},  # call context
        )

    def post(self, request, rating):
        return redirect(reverse('thankyou'))


class ThankyouView(TemplateView):
    template = 'thankyou.html'

    def get(self, request):
        return render(
            request,
            self.template,
        )
