from django.shortcuts import render
from django.http import JsonResponse
from .models import Operacion
import json

def index(request):
    return render(request, "CalculadoraWebApp/index.html")



def guardar_operacion(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        operacion = data.get('operacion')
        resultado = data.get('resultado')
        Operacion.objects.create(operacion=operacion, resultado=resultado)
        return JsonResponse({'message': 'Operación guardada correctamente'}, status=201)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)