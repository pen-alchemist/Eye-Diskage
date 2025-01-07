from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny

from backend.models import BlogPost


@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny,])
def blog_collection_view(request):
    """Returns all Blog Posts with pagination (10 per page) using JSONResponse"""

    posts_list = []

    posts = BlogPost.objects.all()

    for post in posts:
        _slug = getattr(post, 'post_slug')
        _content = getattr(post, 'post_content')
        _date = getattr(post, 'created_date')
        _img = getattr(post, 'post_image')
        date_str = _date.strftime('%Y-%m-%d')
        short_content = f'{_content[0:400]}...'
        posts_list.append(
            {
                'post_content_short': short_content,
                'post_slug': _slug,
                'post_date': date_str,
                'post_image': _img.url,
            }
        )

    paginator = Paginator(posts_list, 10)
    page = request.GET.get('page', 1)
    try:
        items_page = paginator.page(page)
    except (PageNotAnInteger, EmptyPage) as page_e:
        items_page = paginator.page(paginator.num_pages)

    response = {
        'posts': list(items_page),
        'is_next': items_page.has_next(),
        'is_previous': items_page.has_previous(),
        'current': items_page.number,
        'pages_count': paginator.num_pages,
        'posts_count': len(posts),
    }

    return JsonResponse(response)


@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny,])
def blog_reading_view(request, slug):
    """Returns 1 Blog Post (title, content, date, image) using JSONResponse"""

    post = get_object_or_404(BlogPost, post_slug=slug)
    _date = getattr(post, 'created_date')
    _img = getattr(post, 'post_image')
    date_str = _date.strftime('%Y-%m-%d')

    data = {
        'post_title': getattr(post, 'post_title'),
        'post_content': getattr(post, 'post_content'),
        'post_date': date_str,
        'post_image': _img.url,
    }
    response = {
        'data': data
    }

    return JsonResponse(response)
