import json
import datetime
import resource

from django.test import TestCase
from django.contrib.contenttypes.models import ContentType

from rest_framework.test import APIRequestFactory

from backend.models import BlogPost
from backend.tests.config.config_make_string import make_random_string
from backend.tests.config.config_make_string import random_string_no_special_char
from backend.views import post_read_view


class TestPostReadEndpoint(TestCase):

    def setUp(self):
        """Testing setup. Returns Read Post API factory object"""

        # Clear all cache at once for all cases
        ContentType.objects.clear_cache()

        self.random_title = make_random_string(200)
        self.random_slug = random_string_no_special_char(30)
        self.random_content = make_random_string(4000)
        self.url = f'/blog/api/blog/read/{self.random_slug}/'

        # Creating Blog Post Object in database
        self.blog_post = BlogPost.objects.create(
            post_title=self.random_title,
            post_slug=self.random_slug,
            post_content=self.random_content
        )

        self.factory = APIRequestFactory()
        self.request = self.factory.get(self.url)
        self.response = post_read_view(self.request, self.random_slug)
        self.json_data = json.loads(self.response.content)

        return self.json_data

    def tearDown(self):
        """Testing setup. Deleting blog post object"""

        # Clear all cache at once for all cases
        ContentType.objects.clear_cache()
        print('Cache was cleared')

        mb_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000
        print(f'Memory usage: {mb_memory} MB')

        self.blog_post.delete()
        del self.json_data
        print('All testing data was cleared')

    def test_post_read_response_status(self):
        """Test that read post endpoint returns 200 status code"""

        self.assertEqual(self.response.status_code, 200)

    def test_main_page_title_field_value(self):
        """Test that read post endpoint returns correct title value"""

        post_title = self.json_data['post_title']

        self.assertEqual(post_title, self.random_title)

    def test_main_page_title_field_len_max(self):
        """Test that read post endpoint returns
        correct title len smaller or equal 200"""

        post_title = self.json_data['post_title']

        self.assertTrue(len(post_title) <= 200)

    def test_main_page_title_field_len_min(self):
        """Test that read post endpoint returns
        correct title len bigger than 0"""

        post_title = self.json_data['post_title']

        self.assertTrue(len(post_title) > 0)

    def test_post_read_content_full_field_value(self):
        """Test that read post endpoint
        returns correct short content value"""

        post_content_full = self.json_data['post_content']

        self.assertEqual(post_content_full, self.random_content)

    def test_post_read_content_full_field_max_len(self):
        """Test that read post endpoint returns
        correct short content smaller or equal 4000"""

        post_content_full = self.json_data['post_content']

        self.assertTrue(len(post_content_full) <= 4000)

    def test_post_read_date_field(self):
        """Test that read post endpoint returns correct date"""

        date_actual = self.json_data['post_date']
        date_expected = datetime.datetime.now().strftime('%Y-%m-%d')

        self.assertEqual(date_actual, date_expected)

    def test_post_read_null_image_field(self):
        """Test that read post endpoint returns correct null image"""

        post_image = self.json_data['post_image']

        self.assertEqual(post_image, '""')
