from rest_framework import serializers
from .models import datos, estudiante

class PlanSerializer(serializers.ModelSerializer):
    numro_estudiante = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model  = datos
        fields = ["id", "nombre", "matricula", "nota", "materia"]

    def get_total_socios(self, obj):
        return obj.socios.filter(activo=True).count()

class SocioSerializer(serializers.ModelSerializer):
    estudiante_matricula = serializers.CharField(source="estudiante.nombre", read_only=True)

    class Meta:
        model  = estudiante
        fields = ["id", "estudiante", "estudiante_matricula", "nombre", "matricula",
                  "nota_parcial", "nota_final", "aprobado"]