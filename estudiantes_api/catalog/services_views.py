from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def cobros_view(request):
    datos = request.data.get("datos", [])

    if not isinstance(datos, list) or len(datos) == 0:
        return Response(
            {"detail": "El campo 'datos' debe ser una lista no vacía."},
            status=status.HTTP_400_BAD_REQUEST
        )

    total_cobro = 0
    detalle     = []

    for datos in datos:
        nombre      = datos.get("nombre", "")
        matricula       = float(datos.get("cuota", 0))
        nota = int(datos.get("dias_atraso", 0))

        # Determinar porcentaje de recargo según días de atraso
        if nota == 0:
            nota_parcial = 0
        elif nota <= 7:
            nota_final = 5
        elif nota <= 15:
            aprobado = 10
        else:
            aprobado = 20

        nota_final     = round(matricula * nota_parcial / 100, 2)
        nota_parcial = round(matricula + nota_final, 2)
        total_notas = round(total_cobro +  aprobado, 2)

        detalle.append({
            "nombre":      nombre,
            "nota": nota_parcial,
            "total_notas": nota_final,
        })

    return Response({
        "nota_parcial": len(detalle),
        "nota_final":  total_nota,
        "detalle":      detalle,
    })