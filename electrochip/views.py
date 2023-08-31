from django.shortcuts import render
from .models import Services

# Create your views here.


def index(request):
    # service1 = Services()
    # service1.title = 'Equipment installation'
    # service1.desc = 'There are many variations of passages of Lorem Ipsum available'
    # service1.img = 's1.png'
    # service1.spc = False


    # service2 = Services()
    # service2.title = 'Windmill Energy'
    # service2.desc = 'There are many variations of passages of Lorem Ipsum available,'
    # service2.img = 's2.png'
    # service2.spc = False


    # service3 = Services()
    # service3.title = 'Offshore Engineering'
    # service3.desc = 'There are many variations of passages of Lorem Ipsum available,'
    # service3.img = 's3.png'
    # service3.spc = False


    # service4 = Services()
    # service4.title = 'Electrical Wiring'
    # service4.desc = 'There are many variations of passages of Lorem Ipsum available,'
    # service4.img = 's4.png'
    # service4.spc = True


    # slist = [service1 , service2 ,service3 , service4]

    slist = Services.objects.all()

    return render(request,'index.html' ,{'slist':slist})

