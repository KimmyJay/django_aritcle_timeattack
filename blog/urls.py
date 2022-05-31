from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('new/', views.new, name='article'),
    path('detail/<int:id>', views.detail, name='detail'),
    # path('tweet/<int:id>', views.detail_tweet, name='detail-tweet'),
    # path('tweet/comment/<int:id>', views.write_comment, name='write-comment'),
    # path('tweet/comment/delete/<int:id>', views.delete_comment, name='delete-comment'),
]