import datetime
import json
import resource

from django.test import TestCase
from django.contrib.contenttypes.models import ContentType

from rest_framework.test import APIRequestFactory

from backend.models import BlogPost
from backend.tests.config.config_make_string import make_random_string
from backend.views import blog_collection_view


class TestAllBlogsEndpoint(TestCase):

    def setUp(self):
        """Testing setup. Returns API factory object"""

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

        self.factory = APIRequestFactory()

        return self.factory

    def tearDown(self):
        """Testing setup. Deleting blog post object"""

        # Clear all cache at once for all cases
        ContentType.objects.clear_cache()
        print('Cache was cleared')

        mb_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000
        print(f'Memory usage: {mb_memory} MB')

        del self.factory
        print('All testing data was cleared')

    def test_posts_all_response_status(self):
        """Test that posts collection view returns 200 status code"""

        request = self.factory.get('/blog/api/blog/all/')
        response = blog_collection_view(request)

        self.assertEqual(response.status_code, 200)

    def test_posts_all_title_field(self):
        """Test that posts collection view returns correct title"""

        request = self.factory.get('/blog/api/blog/all/')
        response = blog_collection_view(request)
        json_data = json.loads(response.content)
        post_title = json_data['posts'][0]['post_title']

        self.assertEqual(post_title, self.random_title)
        self.assertTrue(len(post_title) <= 200)
        self.assertTrue(len(post_title) > 0)

    def test_posts_all_content_short_field(self):
        """Test that posts collection view returns correct short content"""

        request = self.factory.get('/blog/api/blog/all/')
        response = blog_collection_view(request)
        json_data = json.loads(response.content)
        post_content_actual = json_data['posts'][0]['post_content_short']
        post_content_expected = f'{self.random_content[0:400]}...'


        self.assertEqual(post_content_actual, post_content_expected)
        self.assertNotEqual(post_content_actual, self.random_content)
        self.assertEqual(len(post_content_actual), 403)

    def test_posts_all_slug_field(self):
        """Test that posts collection view returns correct slug"""

        request = self.factory.get('/blog/api/blog/all/')
        response = blog_collection_view(request)
        json_data = json.loads(response.content)
        post_slug = json_data['posts'][0]['post_slug']

        self.assertEqual(post_slug, self.random_slug)
        self.assertTrue(len(post_slug) <= 30)
        self.assertTrue(len(post_slug) > 0)

    def test_posts_all_date_field(self):
        """Test that posts collection view returns correct date"""

        request = self.factory.get('/blog/api/blog/all/')
        response = blog_collection_view(request)
        json_data = json.loads(response.content)
        date_actual = json_data['posts'][0]['post_date']
        date_expected = datetime.datetime.now().strftime('%Y-%m-%d')

        self.assertEqual(date_actual, date_expected)

    def test_posts_all_null_image_field(self):
        """Test that posts collection view returns correct null image"""

        request = self.factory.get('/blog/api/blog/all/')
        response = blog_collection_view(request)
        json_data = json.loads(response.content)
        post_image = json_data['posts'][0]['post_image']

        self.assertEqual(post_image, '""')

    def test_posts_all_no_next_page_field(self):
        """Test that posts collection view returns no next page (false)"""

        request = self.factory.get('/blog/api/blog/all/')
        response = blog_collection_view(request)
        json_data = json.loads(response.content)
        is_next = json_data['is_next']

        self.assertFalse(is_next)

    def test_posts_all_no_previous_page_field(self):
        """Test that posts collection view returns no previous page (false)"""

        request = self.factory.get('/blog/api/blog/all/')
        response = blog_collection_view(request)
        json_data = json.loads(response.content)
        is_previous = json_data['is_previous']

        self.assertFalse(is_previous)

    def test_posts_all_number_of_current_page_field(self):
        """Test that posts collection view returns current page number"""

        request = self.factory.get('/blog/api/blog/all/')
        response = blog_collection_view(request)
        json_data = json.loads(response.content)
        current = json_data['current']

        self.assertEqual(current, 1)

    def test_posts_all_number_of_pages_count_field(self):
        """Test that posts collection view returns number of pages"""

        request = self.factory.get('/blog/api/blog/all/')
        response = blog_collection_view(request)
        json_data = json.loads(response.content)
        pages_count = json_data['pages_count']

        self.assertEqual(pages_count, 1)

    def test_posts_all_number_of_posts_count_field(self):
        """Test that posts collection view returns number of posts"""

        request = self.factory.get('/blog/api/blog/all/')
        response = blog_collection_view(request)
        json_data = json.loads(response.content)
        posts_count = json_data['posts_count']

        self.assertEqual(posts_count, 1)

