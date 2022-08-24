from django.shortcuts import render
from Apps.models import Familiares
from datetime import datetime

def Familiares_v(request):

    fecha = datetime.now()

    Familiares1 = Familiares(Nombre='Sebastian', Apellido='Gossos', Año_de_nacimiento=1999,
                             Email='winigossos@gmail.com', Fecha_actual=fecha)
    Familiares1.save()

    Familiares2 = Familiares(Nombre='Marisa', Apellido='Gossos', Año_de_nacimiento=1969,
                             Email='Marisagossos@gmail.com', Fecha_actual=fecha)
    Familiares2.save()

    Familiares3 = Familiares(Nombre='Maria', Apellido='Gossos', Año_de_nacimiento=1994,
                             Email='Mariagossos@gmail.com', Fecha_actual=fecha)
    Familiares3.save()
    contexto = {
        'familiares1': Familiares1,
        'familiares2': Familiares2,
        'familiares3': Familiares3
    }

    return render(request, 'Template_2.html', contexto)
