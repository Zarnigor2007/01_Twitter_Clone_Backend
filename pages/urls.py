from django.urls import path
from .views import Homepage, user_profile

urlpatterns = [
    path('', Homepage, name='home'),
    path('profile/<str:username>/', user_profile, name='user_profile'),
]
