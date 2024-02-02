from .models import CatchUser, Deadline
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils import timezone



def register(request):
    last_time = Deadline.objects.all().last()
    if last_time.datetime > timezone.now():
        print("Hello")
        if request.method == "POST":
            first_name = request.POST.get('first_name')
            phone_number = request.POST.get('phone_number')
            password = "Pass!123"
            print(phone_number)
            print(first_name)

            user = CatchUser.objects.filter(username=phone_number)

            if user.exists():
                messages.warning(request, "User already exists!")
                return redirect('/')
            else:
                instance = CatchUser.objects.create_user(username=phone_number, password=password, first_name=first_name)
                user = authenticate(username=phone_number, password=password, first_name=first_name)
                if user is not None:
                    login(request, user)
                messages.success(request, 'Your account has been created!')
                return redirect("/")
        else:
            
            if request.user.is_authenticated:
                print("Work!!!!!!!!!")
                user = request.user
                user.enter_the_vebinar = True
                user.save()
            else:
                print("!!!!!Don't Work!!!!!!")
                pass
    return render(request, 'index.html', {'date_time': last_time, 'request': request})
