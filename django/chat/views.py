from .forms import CustomUserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import render, redirect


def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chat/chatPage.html", context)


def custom_logout(request):
    logout(request)
    return redirect('/')  # 'home'은 홈페이지의 URL 이름입니다.


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login-user')  # 사용자 생성 후 로그인 페이지로 리다이렉트
    template_name = 'chat/signup.html'
