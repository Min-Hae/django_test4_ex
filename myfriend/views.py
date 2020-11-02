from django.shortcuts import render
from myfriend.models import Friends

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def showFriendFunc(request):
    datas = Friends.objects.all()
    
    return render(request, 'show.html', {'friendslist' : datas})