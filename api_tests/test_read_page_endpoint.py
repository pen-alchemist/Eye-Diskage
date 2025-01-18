import json
import datetime
import resource

from django.test import TestCase
from django.contrib.contenttypes.models import ContentType

from rest_framework.test import APIRequestFactory

from backend.models import BlogPost
from backend.tests.config.config_make_string import make_random_string
from backend.views import post_read_view


class TestPostReadEndpoint(TestCase):

    def setUp(self):
        """Testing setup. Returns Read Post API factory object"""

        # Clear all cache at once for all cases
        ContentType.objects.clear_cache()

        self.random_title = make_random_string(200)
        self.random_slug = make_random_string(30)
        self.random_content = make_random_string(4000)
        self.url = f'/blog/api/blog/read/{self.random_slug}/'

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

    def test_post_read_response_status(self):
        """Test that posts collection endpoint returns 200 status code"""

        request = self.factory.get(self.url)
        response = post_read_view(request, self.random_slug)

        self.assertEqual(response.status_code, 200)

    def test_post_read_title_field(self):
        """Test that posts collection endpoint returns correct title"""

        request = self.factory.get(self.url)
        response = post_read_view(request, self.random_slug)
        json_data = json.loads(response.content)
        post_title = json_data['post_title']

        self.assertEqual(post_title, self.random_title)
        self.assertTrue(len(post_title) <= 200)
        self.assertTrue(len(post_title) > 0)

    def test_post_read_content_full_field(self):
        """Test that posts collection endpoint returns correct short content"""

        request = self.factory.get(self.url)
        response = post_read_view(request, self.random_slug)
        json_data = json.loads(response.content)
        post_content_full = json_data['post_content']


        self.assertEqual(post_content_full, self.random_content)
        self.assertTrue(len(post_content_full) <= 4000)

    def test_post_read_date_field(self):
        """Test that posts collection endpoint returns correct date"""

        request = self.factory.get(self.url)
        response = post_read_view(request, self.random_slug)
        json_data = json.loads(response.content)
        date_actual = json_data['post_date']
        date_expected = datetime.datetime.now().strftime('%Y-%m-%d')

        self.assertEqual(date_actual, date_expected)

    def test_post_read_null_image_field(self):
        """Test that posts collection endpoint returns correct null image"""

        request = self.factory.get(self.url)
        response = post_read_view(request, self.random_slug)
        json_data = json.loads(response.content)
        post_image = json_data['post_image']

        self.assertEqual(post_image, '""')
