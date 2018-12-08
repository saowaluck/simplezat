from django.urls import reverse
from django.test import TestCase


class RatingViewTest(TestCase):
    def setUp(self):
        self.url = reverse('ratings')

    def test_reating_view_should_be_accessable(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_rating_view_should_view_question_text(self):
        response = self.client.get(self.url)

        expected = '<h1>How do we do?</h1>'
        self.assertContains(response, expected, status_code=200)

