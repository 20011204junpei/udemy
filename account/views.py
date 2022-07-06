from re import template
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import (
     get_user_model, logout as auth_logout,
)
from requests import request
from .forms import UserCreateForm

from .models import Article, Post
from .forms import AddForm


User = get_user_model()


class IndexView(generic.TemplateView):
    template_name = 'top.html'


class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileView(LoginRequiredMixin, generic.View):

    def get(self, *args, **kwargs):
        return render(self.request,'registration/profile.html')

class BlogView(generic.ListView):
    model = Article
    paginate_by = 5

    template_name = 'registration/post_list.html'
    success_url = reverse_lazy('accounts:post_list')

    def get_queryset(self):
        #最新記事を上にするための記述
        return Post.objects.order_by('-created_at')


class AddView(generic.CreateView):
    model = Post
    form_class = AddForm
    template_name = 'registration/add.html'
    success_url = reverse_lazy('accounts:post_list')
    
class UpdateArticle(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = AddForm
    template_name = 'registration/add.html'
    success_url=reverse_lazy('accounts:post_list')

class DeleteArticle(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'registration/post_confirm_delete.html'
    success_url=reverse_lazy('accounts:post_list')

class DetailArticle(generic.DetailView):
    model = Post
    template_name = 'registration/post_detail.html'
        
class DeleteView(LoginRequiredMixin, generic.View):

    def get(self, *args, **kwargs):
        user = User.objects.get(email=self.request.user.email)
        user.is_active = False
        user.save()
        auth_logout(self.request)
        return render(self.request,'registration/delete_complete.html')
