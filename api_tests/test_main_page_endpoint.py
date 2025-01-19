import json
import datetime
import resource

from django.test import TestCase
from django.contrib.contenttypes.models import ContentType

from rest_framework.test import APIRequestFactory

from backend.models import BlogPost
from backend.tests.config.config_make_string import make_random_string
from backend.views import main_page_view


class TestMainPageEndpoint(TestCase):

    def setUp(self):
        """Testing setup. Returns Main Page API factory object"""

        # Clear all cache at once for all cases
        ContentType.objects.clear_cache()

        self.random_title = make_random_string(200)
        self.random_slug = make_random_string(30)
        self.random_content = make_random_string(4000)
        self.url = '/blog/api/blog/all/'

        # Creating Blog Post Object in database
        self.blog_post = BlogPost.objects.create(
            post_title=self.random_title,
            post_slug=self.random_slug,
            post_content=self.random_content
        )

        self.factory = APIRequestFactory()
        self.request = self.factory.get(self.url)
        self.response = main_page_view(self.request)

        return self.response

    def tearDown(self):
        """Testing setup. Deleting blog post object"""

        # Clear all cache at once for all cases
        ContentType.objects.clear_cache()
        print('Cache was cleared')

        mb_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000
        print(f'Memory usage: {mb_memory} MB')

        self.blog_post.delete()
        del self.response
        print('All testing data was cleared')

    def test_main_page_response_status(self):
        """Test that posts collection endpoint returns 200 status code"""

        self.assertEqual(self.response.status_code, 200)

    def test_main_page_title_field_value(self):
        """Test that posts collection endpoint returns correct title value"""

        json_data = json.loads(self.response.content)
        post_title = json_data['posts'][0]['post_title']

        self.assertEqual(post_title, self.random_title)

    def test_main_page_title_field_len_max(self):
        """Test that posts collection endpoint
        returns correct title len smaller or equal 200"""

        json_data = json.loads(self.response.content)
        post_title = json_data['posts'][0]['post_title']

        self.assertTrue(len(post_title) <= 200)

    def test_main_page_title_field_len_min(self):
        """Test that posts collection endpoint
        returns correct title len bigger than 0"""

        json_data = json.loads(self.response.content)
        post_title = json_data['posts'][0]['post_title']

        self.assertTrue(len(post_title) > 0)

    def test_main_page_content_short_field_value(self):
        """Test that posts collection endpoint returns short content value"""

        json_data = json.loads(self.response.content)
        post_content_actual = json_data['posts'][0]['post_content_short']
        post_content_expected = f'{self.random_content[0:400]}...'

        self.assertEqual(post_content_actual, post_content_expected)

    def test_main_page_content_short_field_not_full(self):
        """Test that posts collection endpoint returns shorted content"""

        json_data = json.loads(self.response.content)
        post_content_actual = json_data['posts'][0]['post_content_short']

        self.assertNotEqual(post_content_actual, self.random_content)

    def test_main_page_content_short_field_len(self):
        """Test that posts collection endpoint
        returns content with len equal 403"""

        json_data = json.loads(self.response.content)
        post_content_actual = json_data['posts'][0]['post_content_short']

        self.assertEqual(len(post_content_actual), 403)

    def test_main_page_slug_field_value(self):
        """Test that posts collection endpoint returns correct slug value"""

        json_data = json.loads(self.response.content)
        post_slug = json_data['posts'][0]['post_slug']

        self.assertEqual(post_slug, self.random_slug)

    def test_main_page_slug_field_len_max(self):
        """Test that posts collection endpoint
        returns slug with len smaller or equal 30"""

        json_data = json.loads(self.response.content)
        post_slug = json_data['posts'][0]['post_slug']

        self.assertTrue(len(post_slug) <= 30)

    def test_main_page_slug_field_len_min(self):
        """Test that posts collection endpoint
        returns slug with len bigger than 0"""

        json_data = json.loads(self.response.content)
        post_slug = json_data['posts'][0]['post_slug']

        self.assertTrue(len(post_slug) > 0)

    def test_main_page_date_field(self):
        """Test that posts collection endpoint returns correct date"""

        json_data = json.loads(self.response.content)
        date_actual = json_data['posts'][0]['post_date']
        date_expected = datetime.datetime.now().strftime('%Y-%m-%d')

        self.assertEqual(date_actual, date_expected)

    def test_main_page_null_image_field(self):
        """Test that posts collection endpoint returns correct null image"""

        json_data = json.loads(self.response.content)
        post_image = json_data['posts'][0]['post_image']

        self.assertEqual(post_image, '""')

    def test_main_page_no_next_page_field(self):
        """Test that posts collection endpoint returns no next page (false)"""

        json_data = json.loads(self.response.content)
        is_next = json_data['is_next']

        self.assertFalse(is_next)

    def test_main_page_no_previous_page_field(self):
        """Test that posts collection endpoint returns no previous page (false)"""

        json_data = json.loads(self.response.content)
        is_previous = json_data['is_previous']

        self.assertFalse(is_previous)

    def test_main_page_number_of_current_page_field(self):
        """Test that posts collection endpoint returns current page number"""

        json_data = json.loads(self.response.content)
        current = json_data['current']

        self.assertEqual(current, 1)

    def test_main_page_number_of_pages_count_field(self):
        """Test that posts collection endpoint returns number of pages"""

        json_data = json.loads(self.response.content)
        pages_count = json_data['pages_count']

        self.assertEqual(pages_count, 1)

    def test_main_page_number_of_posts_count_field(self):
        """Test that posts collection endpoint returns number of posts"""

        json_data = json.loads(self.response.content)
        posts_count = json_data['posts_count']

        self.assertEqual(posts_count, 1)

