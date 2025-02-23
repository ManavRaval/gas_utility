
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, signup

urlpatterns = [
    path('', home, name='home'),  # Home route
    path('home/', home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='customers/login.html'), name='login'),
    path('signup/', signup, name='signup'),
]


