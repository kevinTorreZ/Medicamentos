from django.shortcuts import render
def index(request): 
    return render(request,'index.html')

def productos(request): 
    return render(request,'Productos.html')


def cuenta(request): 
    return render(request,'Cuenta.html')


def registrado(request): 
    return render(request,'Registrado.html')



# Create your views here.
