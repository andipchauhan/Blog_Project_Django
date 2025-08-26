from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.

class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
     
# def index(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3] # dajngo will convert this into SQL and only retrieve the latest 3 instead of all and then slicing, NO NEGATIVE INDEXING
#     return render(request, 'blog/index.html', {
#         "posts": latest_posts
#     })


class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "all_posts"
    ordering = ["-date"]

# def posts(request):
#     all_posts= Post.objects.all().order_by("-date")
#     return render(request, 'blog/all-posts.html',{
#         "all_posts": all_posts
#     })


class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tag.all()
        return context

# def post_detail(request, post_slug):
#     # target_post = Post.objects.get(slug=post_slug)
#     target_post = get_object_or_404(Post, slug=post_slug)
#     return render(request, 'blog/post-detail.html',{
#         "post": target_post,
#         "post_tags": target_post.tag.all()
#     })