from django.test import TestCase
from django.contrib.auth import get_user_model
from news.models import Post
# Create your tests here.


class TestNewsViews(TestCase):

    def test_news_home_page(self):
        page = self.client.get('/news/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'news_home.html')

    def test_news_article_page(self):
        user = get_user_model().objects.create(username='testuser')
        post = Post.objects.create(author=user,
                                   title='testpost',
                                   sub_title='testsub',
                                   slug='testslug',
                                   image='test.png',
                                   preview_text='preview',
                                   content='content',
                                   featured=False)

        page = self.client.get('/news/'+post.slug+'/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'news_article.html')
