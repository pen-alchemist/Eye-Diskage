import uuid
import resource

from unittest.mock import Mock

from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from backend.models import BlogPost
from backend.admin import BlogPostAdmin

from backend.tests.config.config_make_string import make_random_string
from backend.tests.config.config_user_random import make_random_username
from backend.tests.config.config_user_random import make_random_first_name
from backend.tests.config.config_user_random import make_random_last_name
from backend.tests.config.config_user_random import make_random_email
from backend.tests.config.config_user_random import make_random_password


class TestBlogPostAdmin(TestCase):

    def setUp(self):
        """Testing setup. Returns blog post object"""

        # Clear all cache at once for all cases
        ContentType.objects.clear_cache()

        self.random_username = make_random_username()
        self.random_first_name = make_random_first_name()
        self.random_last_name = make_random_last_name()
        self.random_email = make_random_email()
        self.random_password = make_random_password()

        self.random_title = make_random_string(200)
        self.random_slug = make_random_string(30)
        self.random_content = make_random_string(4000)

        self.random_title = make_random_string(200)
        self.random_slug = make_random_string(30)
        self.random_content = make_random_string(4000)

        self.blog_model_admin = BlogPostAdmin(model=BlogPost, admin_site=AdminSite())

        self.new_user = User.objects.create(
            username=self.random_username,
            first_name=self.random_first_name,
            last_name=self.random_last_name,
            email=self.random_email,
            password=self.random_password
        )

        self.blog_model_admin.save_model(
            obj=BlogPost(
                post_title=self.random_title,
                post_slug=self.random_slug,
                post_content=self.random_content
            ),
            request=Mock(
                user=self.new_user
            ),
            form=None,
            change=None
        )

        return self.blog_model_admin

    def tearDown(self):
        """Testing teardown. Deleting blog post object"""

        # Clear all cache at once for all cases
        ContentType.objects.clear_cache()
        print('Cache was cleared')

        mb_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000
        print(f'Memory usage: {mb_memory} MB')

        del self.new_user
        del self.blog_model_admin
        print('All testing data was cleared')

    def test_post_admin_title_field(self):
        """Test that post title is correct"""

        post_title = BlogPost.objects.all()[0].post_title

        self.assertEqual(post_title, self.random_title)

    def test_post_admin_slug_field(self):
        """Test that post slug is correct"""

        post_slug = BlogPost.objects.all()[0].post_slug

        self.assertEqual(post_slug, self.random_slug)

    def test_post_admin_content_field(self):
        """Test that post content is correct"""

        post_content = BlogPost.objects.all()[0].post_content

        self.assertEqual(post_content, self.random_content)

    def test_post_admin_str_method(self):
        """Test that post str method returns correct value (post title)"""

        post_str = BlogPost.objects.all()[0].__str__()

        self.assertEqual(post_str, self.random_title)

    def test_post_admin_get_post_pk_type(self):
        """Test that post get_post_pk method returns correct type (uuid)"""

        post_pk = BlogPost.objects.all()[0].get_post_pk()

        self.assertEqual(type(post_pk), uuid.UUID)
