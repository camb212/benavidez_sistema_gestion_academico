from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PlanViewSet, SocioViewSet
from .services_views import cobros_view, clases_view

router = DefaultRouter()
router.register(r"datos", PlanViewSet,  basename="datos")
router.register(r"estudiante", SocioViewSet, basename="estudiante")

urlpatterns = [
    path("estudiante/matricula/", cobros_view),   # POST — FOR
    path("nota/aprobado/", clases_view),   # GET  — WHILE
]

urlpatterns += router.urls