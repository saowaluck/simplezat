from django.urls import reverse
from django.test import TestCase


class RatingViewTest(TestCase):
    def setUp(self):
        self.url = reverse('ratings')

    def test_rating_view_should_view_question_text(self):
        response = self.client.get(self.url)

        expected = '<h1>How do we do?</h1>'
        self.assertContains(response, expected, status_code=200)

    def test_rating_view_should_show_three_rating(self):
        response = self.client.get(self.url)

        positive = '<a href="ratings/positive/">'\
            '<img src="/static/images/positive.png" alt="Positive"></a>'
        neutral = '<a href="ratings/neutral/">'\
            '<img src="/static/images/neutral.png" alt="Neutral"></a>'
        negative = '<a href="ratings/negative/">'\
            '<img src="/static/images/negative.png" alt="Negative"></a>'
        self.assertContains(response, positive, status_code=200)
        self.assertContains(response, neutral, status_code=200)
        self.assertContains(response, negative, status_code=200)
