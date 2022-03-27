from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='index'),
        path('add_post/',views.new_post,name='new_post'),
    path('detail/<int:post_id>/',views.detail_post,name='detail')
]