from django.urls import path 
from . import views
from .views import CreatePostView ,UpdatePostView , DeletePostView
urlpatterns = [
    path('',views.index,name='index'),
    path('new_post/',CreatePostView.as_view(),name='new_post'),
    path('detail/<int:post_id>/',views.detail_post,name='detail'),
    path('detail/<slug:pk>/update/',UpdatePostView.as_view(),name='update_post'),
    path('detail/<slug:pk>/delete/',DeletePostView.as_view(),name='delete_post'),
] 