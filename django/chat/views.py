from django.shortcuts import render, redirect



def chatPage(request, *args, **kwargs):
	if not request.user.is_authenticated:
		return redirect("login-user")
	context = {}
	return render(request, "chat/chatPage.html", context)


from django.contrib.auth import logout

def custom_logout(request):
    logout(request)
    return redirect('/')  # 'home'은 홈페이지의 URL 이름입니다.
