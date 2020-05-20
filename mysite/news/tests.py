import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Article

def create_article(article_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Article.objects.create(question_text=article_text, pub_date=time)

class ArticleModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_article = Article(pub_date=time)
        self.assertIs(future_article.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_article = Article(pub_date=time)
        self.assertIs(old_article.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_article = Article(pub_date=time)
        self.assertIs(recent_article.was_published_recently(), True)

class DetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_article = create_article(headline='Future Article.', days=5)
        url = reverse('news:all_article', args=(future_article.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_article(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_article = create_article(headline='Past Article.', days=-5)
        url = reverse('news:all_article', args=(past_article.id,))
        response = self.client.get(url)
        self.assertContains(response, past_article.headline)