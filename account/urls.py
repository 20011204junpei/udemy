from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'accounts'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('post_list/',views.BlogView.as_view(),name='post_list'),
    path('add/',views.AddView.as_view(),name='add'),
    path('update_article/<int:pk>/',views.UpdateArticle.as_view(),name='update_article'),
    path('delete_article/<int:pk>/',views.DeleteArticle.as_view(),name='delete_article'),
    path('deyail_article/<int:pk>/',views.DetailArticle.as_view(),name='detail_article'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('delete_confirm', TemplateView.as_view(template_name='registration/delete_confirm.html'), name='delete-confirmation'),
    path('delete_complete', views.DeleteView.as_view(), name='delete-complete'),
]