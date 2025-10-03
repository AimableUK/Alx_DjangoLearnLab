from django.urls import path
from .views import login, blogs, profile

urlpatterns = [
    path('login/', login, name="login"),
    path('register/', login, name="register"),
    path('blogs/', blogs, name="blogs"),
    path('profile/', profile, name="profile"),
]