from django.shortcuts import render

from.models import Palce
from .models import Details

# Create your views here.
def demo(request):
    obj=Palce.objects.all()
    obj1=Details.objects.all()
    return render(request,"index.html",{'result':obj,'resu':obj1})