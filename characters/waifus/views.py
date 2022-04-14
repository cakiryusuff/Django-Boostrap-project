from django.shortcuts import render
from django.http import HttpResponse
from .models import Waifus
# Create your views here.

# Create your views here.
def waifus(request):
    waifu = Waifus.objects.all()
    context = {
        'waifus' : waifu 
    }
    return render(request,"waifus/waifus.html",context) 
    #waifus/waifus.html yazan yer dosya konumu




























