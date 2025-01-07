import uuid

from django.db import models


class BlogPost(models.Model):
    post_pk = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_title = models.CharField('Title', max_length=200)
    post_slug = models.SlugField(max_length=30, unique=True)
    post_content = models.TextField('Content', max_length=4000)

    post_image = models.ImageField(upload_to='images/')

    # Post model created date
    created_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Time of post creation'
    )

    class Meta:
        get_latest_by = 'created_at'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.post_title

    def get_post_pk(self):
        return self.post_pk
