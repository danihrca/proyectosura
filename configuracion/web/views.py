from django.shortcuts import render

# Create your views here.
#renderizar es pintar
def Home(request):
    return render(request,'index.html')