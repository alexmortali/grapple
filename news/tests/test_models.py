from django.test import TestCase
from news.models import Post
from django.contrib.auth import get_user_model


class TestPostModel(TestCase):

    def test_can_create_a_news_post(self):
        user = get_user_model().objects.create(username='testuser')
        post = Post(author=user,
                    title="Test",
                    sub_title='test',
                    slug='slug',
                    preview_text="preview",
                    content="content",
                    featured=False,
                    )
        post.save()
        self.assertEqual(post.author, user)
        self.assertEqual(post.title, 'Test')
        self.assertEqual(post.sub_title, 'test')
        self.assertEqual(post.slug, 'slug')
        self.assertEqual(post.preview_text, 'preview')
        self.assertEqual(post.content, 'content')
        self.assertEqual(post.featured, False)
