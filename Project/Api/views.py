from django.shortcuts import render
from .forms import *

# Create your views here.
def Home(request):
    return render (request,'Base.html')


def NuevoProductos(request):
    data={
        'Formulario': FormularioProductos()
    }
    if request.method == 'POST':
        formulario = FormularioProductos(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['Mensaje'] = "Producto Guardado Correctamente"
        else:
            data['Mensaje'] = "Error al Guardar el Producto"
    return render(request, 'Pages/NuevoProducto.html', data)