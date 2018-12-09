from django.test import TestCase
from django.urls import reverse


class RatingViewTest(TestCase):
    def setUp(self):
        self.url = reverse('ratings')

    def test_rating_view_should_view_question_text(self):
        response = self.client.get(self.url)

        expected = '<h1>How do we do?</h1>'
        self.assertContains(response, expected, status_code=200)

    def test_rating_view_should_show_three_rating(self):
        response = self.client.get(self.url)

        positive_url = reverse('comments', kwargs={'rating': 'positive'})
        positive = f'<a href="{positive_url}">'\
            '<img src="/static/images/positive.png" alt="Positive"></a>'

        neutral_url = reverse('comments', kwargs={'rating': 'neutral'})
        neutral = f'<a href="{neutral_url}">'\
            '<img src="/static/images/neutral.png" alt="Neutral"></a>'

        negative_url = reverse('comments', kwargs={'rating': 'negative'})
        negative = f'<a href="{negative_url}">'\
            '<img src="/static/images/negative.png" alt="Negative"></a>'

        self.assertContains(response, positive, status_code=200)
        self.assertContains(response, neutral, status_code=200)
        self.assertContains(response, negative, status_code=200)


class CommentViewTest(TestCase):
    def test_comment_view_should_show_text_comment_view_correctly(self):
        for each in ['positive', 'neutral', 'negative']:
            url = reverse('comments', kwargs={'rating': each})
            response = self.client.get(url)

            question_text = '<h1>Any Comment?</h1>'
            self.assertContains(response, question_text, status_code=200)

            form = '<form action="." method="post">' \
                '<input type="hidden" name="csrfmiddlewaretoken"'
            self.assertContains(response, form, status_code=200)

            comment = '<textarea name="comment"></textarea>' \
                f'<input type="hidden" name="rating" value="{each}">' \
                '<input type="submit"></form>\n'
            self.assertContains(response, comment, status_code=200)

    def test_should_redirect_to_thankyou(self):
        url = reverse('comments', kwargs={'rating': 'positive'})
        response = self.client.post(url)
        self.assertRedirects(response, reverse('thankyou'), status_code=302)


class ThankyouViewTest(TestCase):
    def test_should_show_thankyou(self):
        expected = '<h1>Thank you</h1>'
        url = reverse('thankyou')

        response = self.client.get(url)

        self.assertContains(response, expected, status_code=200)
