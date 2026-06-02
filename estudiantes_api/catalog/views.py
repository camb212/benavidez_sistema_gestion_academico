from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Plan, Socio
from .serializers import PlanSerializer, SocioSerializer
from .permissions import IsAdminOrReadOnly

class PlanViewSet(viewsets.ModelViewSet):
    queryset           = Plan.objects.all().order_by("id")
    serializer_class   = PlanSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields      = ["nombre"]
    ordering_fields    = ["id", "nombre", "matricula"]

class SocioViewSet(viewsets.ModelViewSet):
    queryset           = Socio.objects.select_related("plan").all().order_by("nombre")
    serializer_class   = SocioSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ["datos", "estudiante"]
    search_fields      = ["nombre", "matricula"]
    ordering_fields    = ["id", "nombre", "materias"]

    def get_permissions(self):
        # GET /api/socios/ es público sin token
        if self.action == "list":
            return [AllowAny()]
        return super().get_permissions()