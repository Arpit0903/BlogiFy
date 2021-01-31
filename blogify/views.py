from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Blogs, Comment
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django import forms

# Create your views here.
def index(request):
    return render(request, 'index.html')

def LikeView(request, pk):
    post = get_object_or_404(Blogs, id = request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article_detail', args = [str(pk)]))

class HomeView(ListView):
    model = Blogs
    template_name = 'index.html'
    ordering = ['-pub_date']
    paginate_by = 4

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class ArticleView(DetailView):
    model = Blogs
    template_name = 'article_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleView, self).get_context_data(*args, **kwargs)
        comments_connected = Comment.objects.filter(blogs_connected=self.get_object()).order_by('-date_posted')
        context['comments'] = comments_connected
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm(instance=self.request.user)
        
        post = get_object_or_404(Blogs, id = self.kwargs['pk'])

        total_likes = post.get_total_likes()
        liked = False
        
        if post.likes.filter(id = self.request.user.id).exists():
            liked = True
        
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

    def post(self, request, *args, **kwargs):
        new_comment = Comment(comment=request.POST.get('comment'), author=self.request.user, blogs_connected=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)

class UserBlogsView(ListView):
    model = Blogs
    template_name = 'user_posts.html'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Blogs.objects.filter(author=user).order_by('-pub_date')

class MyBlogsView(ListView):
    model = Blogs
    template_name = 'my_blogs.html'

class AddBlogView(CreateView):
    model = Blogs
    template_name = 'add_blog.html'
    fields = ('blog_title', 'blog_content')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateBlogView(UpdateView):
    model = Blogs
    template_name = 'update_blog.html'
    fields = ('blog_title', 'blog_content')

class DeleteBlogView(DeleteView):
    model = Blogs
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home')

