from django.urls import path
from . import views

urlpatterns = [
    path('', views.category, name='category'),
    path('new/', views.new, name='new'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('<str:name>', views.article, name='article'),

]