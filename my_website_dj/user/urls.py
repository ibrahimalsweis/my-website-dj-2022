from django.urls import path 
from . import views
from django.contrib.auth.views import LoginView , LogoutView

from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    # path('logout/',LogoutView.as_view(template_name='user/logout.html'),name='logout')
    # path('login/',LoginView.as_view(template_name='user/signIn.html'),name='login'),


    path('register/',views.register,name='register'),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path('user/profile/',views.profile,name='profile'),
    path('user/profile_update/',views.profile_update,name='profile_update')
]  

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)