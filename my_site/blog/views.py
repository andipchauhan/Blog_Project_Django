from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView
from .forms import CommentForm
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

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


class SinglePostView(View):

    def get(self,request, slug):
        target_post = Post.objects.get(slug=slug)
        context = {
            'post' : target_post,
            'post_tags': target_post.tag.all(),
            'comment_form': CommentForm(),
            'comments': target_post.comments.all().order_by("-id")
        }
        return render(request, 'blog/post-detail.html', context)

    def post(self,request, slug):
        comment_form = CommentForm(request.POST)
        target_post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = target_post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug])) 
        # This will send a get request on this URL, so we dont need to pass context here, instead it will get from render in get()

        context = {
            'post' : target_post,
            'post_tags': target_post.tag.all(),
            'comment_form': comment_form,
            'comments': target_post.comments.all().order_by("-id")
        }
        return render(request, 'blog/post-detail.html', context) 

# def post_detail(request, post_slug):
#     # target_post = Post.objects.get(slug=post_slug)
#     target_post = get_object_or_404(Post, slug=post_slug)
#     return render(request, 'blog/post-detail.html',{
#         "post": target_post,
#         "post_tags": target_post.tag.all()
#     })


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
        return render(request, "blog/stored-posts.html", context)
    
    
    def post(self, request):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is None:
            stored_posts = []
        post_id = int(request.POST["post_id"])
        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect("/")