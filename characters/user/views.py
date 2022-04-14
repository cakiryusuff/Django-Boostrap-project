from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.
def userLogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
    #auth.authenticate aşağıda verilen bilgilerle kayıt var mı yok mu ona bakıyor varsa obje döndürüyor
        user = auth.authenticate(username = username,password = password)
        if user is not None: #eğer user kullanıcısı varsa
            auth.login(request, user) #session id 
            messages.add_message(request,messages.SUCCESS,"Oturum açıldı.")
            return redirect("waifus")#eğer giriş başarılı ise bu sayfayı yönlendiricek
        else:
            messages.add_message(request, messages.ERROR,"Hatalı username yada parola")
            return redirect("login")
    else:
        return render(request,"user/login.html")
def userRegister(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        if password == repassword:
            #username burda daha önceden alınmış kullanıcı adı bilgisi var mı dye database de kontrol edilir
            if User.objects.filter(username = username).exists():
                messages.add_message(request, messages.WARNING,"Bu kullanıcı adı daha önceden alınmış")
                return redirect("register")
            else:
                if User.objects.filter(email = email).exists():
                    messages.add_message(request, messages.WARNING,"Bu email adı daha önceden alınmış")
                    return redirect("register")
                else:
                    # her şey güzel
                    user = User.objects.create_user(username=username,password = password,email=email)
                    user.save()
                    messages.add_message(request, messages.SUCCESS,"Kullanıcı oluşturuldu")

                    return redirect("login")
        else:
            messages.add_message(request, messages.WARNING,"Parolalar eşleşmiyor")
            return redirect("register")
    else:
        return render(request,"user/register.html")

def logout(request):
    if request.method == "POST":
        auth.logout(request) #sessionid yi siliyor
        return redirect("mainpage")
