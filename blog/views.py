from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . models import Post, Comment
from django.contrib.auth.models import User
from .forms import CommentCreateForm
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    context = {
        'posts': posts,
        'form': CommentCreateForm,
        'title':'الصفحة الرئيسية'
    }
    return render(request, 'blog/post_list.html', context)




def author_posts(request, username):
    user = User.objects.get(username=username)
    posts = user.post_set.all().order_by('-date_posted')
    # ordering = ['-date_posted']
    context = {
        'posts': posts,
        'user': user,
        'title':'منشورات' + user.username 
    }

    return render(request, 'blog/authorposts.html', context)



class PostDetail(DetailView):
    model = Post



class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['العنوان', 'المحتوى']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['العنوان', 'المحتوى']

    def form_valid(self, form):
        form.instance.auth = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

@login_required
def comment(request):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=int(request.POST['id']))
        author = request.user
        content = request.POST['content']
        if len(content)>0:
            comment = Comment.objects.create(author=author, post=post, content=content)
            comment.save()
        else:
            pass
        return HttpResponseRedirect(reverse('blog:post', args=(post.id,)))
    return HttpResponseRedirect(reverse('blog:blog-home', args=()))
            
    




def reporters(request):

    return render(request, 'blog/reporters.html', {'title': 'لقاءات'})

