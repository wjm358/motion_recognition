from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib import messages

class HomeView(TemplateView):
    template_name='login.html'


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, '패스워드 변경 성공')
            return redirect('/')
        else:
            messages.error(request, '비밀번호를 정확히 입력하세요')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_change_form.html', {
        'form': form
    })


def password_change(request) :
    if request.method == 'POST':
        print(request.user)
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    return render(request, 'login.html')


def list_video(request) :
    return render(request,'list_video.html')


def search_video(request) :
    q= request.GET.get('search-field','')
    if q:
     return render(request,'search_video.html',{"sq" : q})
    return render(request,'moviemain.html')

def check_login(request) :
    if request.method=='POST':

        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)

            if user.check_password(password):
                login(request,user)
                return HttpResponseRedirect('/moviemain')
            else:
                status ="비밀번호가 틀렸습니다."
                return render(request,'login.html', {"status" : status})

        except User.DoesNotExist:
            status = "존재하지 않는 아이디입니다."

        return render(request,'login.html', {"status":status})


def logout_process(request) :
    request.session['login_id'] = None
    logout(request)
    return render(request,'login.html');


def user_registration(request):
    if request.method == 'POST':
        print("Hello Registration")
        username = request.POST["username"]

        try :
            User.objects.get(username = username)
            status = "이미 저장된 아이디입니다."
            return render(request,'login.html', {"status":status})

        except User.DoesNotExist:
            email = request.POST["email"]
            password = request.POST["password"]

            user = User.objects.create_user(username,email,password)
            user.save()

            request.session["login_id"] = username
            return render(request,'moviemain.html',{"login_id" : username})


def moviemain(request) :
    return render(request, 'moviemain.html')
