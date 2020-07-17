from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'posts/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'posts/blog_post.html'


# def index(request):
#     '''This contains titles of al the blog posts'''
#     all_posts = Post.objects.all()
#     context = {
#         'posts': all_posts
#     }
#     return render(request, 'posts/index.html', context)
#
# def complete_blog(request, slug):
#     '''This returns A completed blog post.'''
#     req_post = Post.objects.get(slug=slug)
#     return render(request, 'posts/blog_post.html', {'post': req_post})
