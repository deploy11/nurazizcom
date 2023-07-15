from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    posts = Portfolio.objects.all()
    if request.method == 'POST':
        Contact.objects.create(
            name = request.POST['name'],
            tel = request.POST['tel'],
            msg = request.POST['msg']
        )
        return redirect('home')
    return render(request,'home.html',{'post':posts})
