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

from .models import Post
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
    model = Post

    success_url = reverse_lazy('post_list')
    template_name = 'registration/post_list.html'

    # model = 'post_list.html'

    def get_queryset(self):
        #最新記事を上にするための記述
        return Post.objects.order_by('-created_at')

    # def get(self, request):
    #     context = {
    #         'post_list':Post.objects.all(),
    #     }
    #     return render(request,'accounts/post_list.html',context)

class AddView(generic.CreateView):
    model = Post
    form_class = AddForm
    # form_class.save()
    template_name = 'registration/add.html'
    success_url = reverse_lazy('accounts:post_list')
    # redirect('accounts:post_list')

class Update(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = AddForm
    template_name = 'registration/add.html'
    success_url=reverse_lazy('accounts:add')

# class Ok(generic.TemplateView):
#     success_url = reverse_lazy('ok')
#     template_name = 'top.html'
        
class DeleteView(LoginRequiredMixin, generic.View):

    def get(self, *args, **kwargs):
        user = User.objects.get(email=self.request.user.email)
        user.is_active = False
        user.save()
        auth_logout(self.request)
        return render(self.request,'registration/delete_complete.html')
