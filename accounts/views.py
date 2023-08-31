from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.


def register(request):


    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        passowrd2 = request.POST['password2']
        email = request.POST['email']

        if password1 == passowrd2:
            if User.objects.filter(username=username).exists():
                print('Username taken')
                messages.info(request,'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print('email taken')
                messages.info(request,'Email taken')
                return redirect('register')


            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')
            
        else:
            print('password not matching')
            messages.info(request,'Passwords not matching')
            return redirect('register')


        
        
       

    
    else:
        return render(request,'register.html')

def login(request):

   
   
    if request.method == 'POST':
       
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username , password = password)

        if user is not None:
            auth.login(request,user) #giving login access to user   
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            print('invalid credentials')
            return redirect('login')
 


    else:
       
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)#logging out the current logged in user
    return redirect('/')
