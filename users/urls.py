from django.urls import path
from .views import login_view, signup_view, profile, update_profile, upload_content, logout_view, like_content
# from .views import 

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('profile/<str:username>', profile, name='profile'),
    path('update-profile', update_profile , name='update-profile'),
    path('upload-content', upload_content , name='upload_content'),
    path('logout', logout_view, name='logout'),
    path('like/<int:content_id>', like_content, name='like')
]