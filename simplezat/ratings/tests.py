from django.test import TestCase


class RatingViewTest(TestCase):
    def test_reating_view_should_be_accessable(self):
        response = self.client.get('/ratings/')
        self.assertEqual(response.status_code, 200)

