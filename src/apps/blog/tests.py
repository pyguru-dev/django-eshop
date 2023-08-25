from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post


class SimplePostsTest(SimpleTestCase):
    def test_post_list_page_status_ok(self):
        response = self.client.get('/blog')
        self.assertEqual(response.status_code, 200)


class PostModelTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(title="This is test")

    def test_title_contain(self):
        post = Post.objects.get(pk=1)
        expected_title_string = f'{post.title}'
        self.assertEqual(expected_title_string, 'This is test')

class BlogTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            password = 'password'
        )
        
        self.post = Post.objects.create(
            title = 'test title',
            body = 'body',
            author = self.user,
        )
        
    def test_title_string_model(self):
        post = Post(title="test title")
        self.assertEqual(str(post), post.title)
        
    def test_post_list(self):
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_list.html")
        
    
    def test_post_detail(self):
        response = self.client.get('/blog/1/')
        self.assertEqual(response.status_code, 200)