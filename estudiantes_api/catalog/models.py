from django.db import models

class datos(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    matricula = models.DecimalField(max_digits=8, decimal_places=2)
    materias = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class estudiante(models.Model):
    nombre        = models.ForeignKey(Plan, on_delete=models.PROTECT, related_name="socios")
    matricula     = models.CharField(max_length=180)
    nota_parcial = models.IntegerField(default=0)
    nota_final      = models.BooleanField(default=True)
    aprobado   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"