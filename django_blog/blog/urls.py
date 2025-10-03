from django.urls import path
from .views import login, blogs

urlpatterns = [
    path('login/', login, name="login"),
    path('blogs/', blogs, name="blogs"),
]