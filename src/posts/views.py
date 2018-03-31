from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *
from .models import *
from profiles.models import Profile

class PostListView(LoginRequiredMixin, View):
    def get(self, request):
        post_list = Post.objects.order_by('-datetime')
        search = request.GET.get('q')
        if search:
            post_list = post_list.filter(Q(title__icontains=search) |
                                         Q(user__username__icontains=search) |
                                         Q(text__icontains=search)
                                        ).distinct()
        paginator = Paginator(post_list, 5)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        return render(request, 'posts/post_list.html', {'posts': posts})

class PostCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        return render(request, 'posts/post_create.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('posts:post_list'))
        return render(request, 'posts/post_create.html', {'form': form})

class PostUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        instance = get_object_or_404(Post, pk=pk)
        form = PostForm(instance=instance)
        return render(request, 'posts/post_update.html', {'form': form})

    def post(self, request, pk):
        instance = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('posts:post_detail', kwargs={'pk': pk}))
        return render(request, 'posts/post_update.html', {'form': form})


class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):        
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'posts/post_delete.html', {'post': post})

    def post(self, request, pk):
        instance = get_object_or_404(Post, pk=pk)
        instance.delete()
        return HttpResponseRedirect(reverse('posts:post_list'))

class PostUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        instance = get_object_or_404(Post, pk=pk)
        form = PostForm(instance=instance)
        return render(request, 'posts/post_update.html', {'form': form})

    def post(self, request, pk):
        instance = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('posts:post_list'))
        return render(request, 'posts/post_update.html', {'form': form})


class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):        
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'posts/post_delete.html', {'post': post})

    def post(self, request, pk):
        instance = get_object_or_404(Post, pk=pk)
        instance.delete()
        return HttpResponseRedirect(reverse('posts:post_list'))

class ProfileViewer(LoginRequiredMixin, View):
    def get(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        if pk == request.user.profile.pk:
            return render(request, 'profiles/profile_view.html', {'profile': profile})
        return render(request, 'posts/profile_viewer.html', {'profile': profile})