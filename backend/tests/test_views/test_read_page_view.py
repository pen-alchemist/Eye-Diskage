import json
import datetime
import resource

from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from backend.models import BlogPost
from backend.tests.config.config_make_string import make_random_string


class TestPostReadView(TestCase):

    def setUp(self):
        """Testing setup. Returns Read Post View Client object"""

        # Clear all cache at once for all cases
        ContentType.objects.clear_cache()

        self.random_title = make_random_string(200)
        self.random_slug = make_random_string(30)
        self.random_content = make_random_string(4000)
        self.client = Client()

        # Creating Blog Post Object in database
        self.blog_post = BlogPost.objects.create(
            post_title=self.random_title,
            post_slug=self.random_slug,
            post_content=self.random_content
        )

        self.response = self.client.get(reverse(
            'blog-reading',
            kwargs = {
                'slug': self.blog_post.post_slug
                }
            )
        )

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

    def test_post_read_response_status(self):
        """Test that posts collection view returns 200 status code"""

        self.assertEqual(self.response.status_code, 200)

    def test_main_page_title_field_value(self):
        """Test that read post view returns correct title value"""

        json_data = json.loads(self.response.content)
        post_title = json_data['post_title']

        self.assertEqual(post_title, self.random_title)

    def test_main_page_title_field_len_max(self):
        """Test that read post view returns
        correct title len smaller or equal 200"""

        json_data = json.loads(self.response.content)
        post_title = json_data['post_title']

        self.assertTrue(len(post_title) <= 200)

    def test_main_page_title_field_len_min(self):
        """Test that read post view returns
        correct title len bigger than 0"""

        json_data = json.loads(self.response.content)
        post_title = json_data['post_title']

        self.assertTrue(len(post_title) > 0)

    def test_post_read_content_full_field_value(self):
        """Test that read post view
        returns correct short content value"""

        json_data = json.loads(self.response.content)
        post_content_full = json_data['post_content']

        self.assertEqual(post_content_full, self.random_content)

    def test_post_read_content_full_field_max_len(self):
        """Test that read post view returns
        correct short content smaller or equal 4000"""

        json_data = json.loads(self.response.content)
        post_content_full = json_data['post_content']

        self.assertTrue(len(post_content_full) <= 4000)

    def test_post_read_date_field(self):
        """Test that posts collection view returns correct date"""

        json_data = json.loads(self.response.content)
        date_actual = json_data['post_date']
        date_expected = datetime.datetime.now().strftime('%Y-%m-%d')

        self.assertEqual(date_actual, date_expected)

    def test_post_read_null_image_field(self):
        """Test that posts collection view returns correct null image"""

        json_data = json.loads(self.response.content)
        post_image = json_data['post_image']

        self.assertEqual(post_image, '""')
