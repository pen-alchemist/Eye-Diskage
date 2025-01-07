import resource

from django.test import TestCase
from django.contrib.contenttypes.models import ContentType

from backend.models import BlogPost
from backend.tests.config.config_make_string import make_random_string


class TestBlogPost(TestCase):

    def setUp(self) -> None:
        # Clear all cache at once for all cases
        ContentType.objects.clear_cache()

        self.random_title = make_random_string(200)
        self.random_slug = make_random_string(30)
        self.random_content = make_random_string(4000)

        # Creating user
        self.user = BlogPost.objects.create(
            post_title=self.random_title,
            post_slug=self.random_slug,
            post_content=self.random_content
        )

        return self.user

    def tearDown(self) -> None:
        # Clear all cache at once for all cases
        ContentType.objects.clear_cache()
        print('Cache was cleared')

        mb_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000
        print(f'Memory usage: {mb_memory} MB')

        del self.user
        print('All testing data was cleared')

    def test_post_title_field(self):
        self.assertEqual(BlogPost.objects.all()[0].post_title, self.random_title)

    def test_post_slug_field(self):
        self.assertEqual(BlogPost.objects.all()[0].post_slug, self.random_slug)

    def test_post_content_field(self):
        self.assertEqual(BlogPost.objects.all()[0].post_content, self.random_content)
