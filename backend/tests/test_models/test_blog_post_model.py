import resource

from django.test import TestCase
from django.contrib.contenttypes.models import ContentType

from backend.models import BlogPost
from backend.tests.config.config_make_string import make_random_string


class TestBlogPost(TestCase):

    def setUp(self):
        """Testing setup. Returns blog post object"""

        # Clear all cache at once for all cases
        ContentType.objects.clear_cache()

        self.random_title = make_random_string(200)
        self.random_slug = make_random_string(30)
        self.random_content = make_random_string(4000)

        # Creating Blog Post object
        self.blog_post = BlogPost.objects.create(
            post_title=self.random_title,
            post_slug=self.random_slug,
            post_content=self.random_content
        )

        return self.blog_post

    def tearDown(self):
        """Testing teardown. Deleting blog post object"""

        # Clear all cache at once for all cases
        ContentType.objects.clear_cache()
        print('Cache was cleared')

        mb_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000
        print(f'Memory usage: {mb_memory} MB')

        del self.blog_post
        print('All testing data was cleared')

    def test_post_title_field(self):
        """Test that post title is correct"""

        post_title = BlogPost.objects.all()[0].post_title

        self.assertEqual(post_title, self.random_title)

    def test_post_slug_field(self):
        """Test that post slug is correct"""

        post_slug = BlogPost.objects.all()[0].post_slug

        self.assertEqual(post_slug, self.random_slug)

    def test_post_content_field(self):
        """Test that post content is correct"""

        post_content = BlogPost.objects.all()[0].post_content

        self.assertEqual(post_content, self.random_content)

    def test_post_str_method(self):
        """Test that post str method returns correct value (post title)"""

        post_str = BlogPost.objects.all()[0].__str__()

        self.assertEqual(post_str, self.random_title)

    def test_post_get_post_pk(self):
        """Test that post get_post_pk method returns correct value (post pk)"""

        post_pk = BlogPost.objects.all()[0].get_post_pk()

        self.assertEqual(post_pk, self.blog_post.pk)
