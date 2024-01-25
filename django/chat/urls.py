from django.urls import path, include
from chat import views as chat_views
from django.contrib.auth.views import LoginView
from .views import SignUpView
urlpatterns = [
    path("", chat_views.chatPage, name="chat-page"),

    # login-section
    path("auth/login/", LoginView.as_view(template_name="chat/LoginPage.html"),
         name="login-user"),
    path('auth/logout/', chat_views.custom_logout, name='logout-user'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
