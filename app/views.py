from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "name": "jjjj",
        "status": False,
    }
    return render(request,'index.html',context)