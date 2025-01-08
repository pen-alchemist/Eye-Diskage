from django import forms

from backend.models import BlogPost


class BlogPostForm(forms.ModelForm):
    post_title = forms.CharField(required=True)
    post_slug = forms.SlugField(required=True)
    post_content = forms.CharField(widget=forms.Textarea, required=True)

    post_image = forms.ImageField(required=False)

    class Meta:
        model = BlogPost
        fields = ('post_title', 'post_slug', 'post_content', 'post_image',)
