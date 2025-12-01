from django.db import models

# -----------------------------
#   MODELO PACIENTE DENTAL
# -----------------------------
class PacienteDental(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    num_seguro_dental = models.CharField(max_length=50)
    fecha_registro = models.DateField()
    historial_medico_previo = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# -----------------------------
#     MODELO ODONTÓLOGO
# -----------------------------
class Odontologo(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    licencia_dental = models.CharField(max_length=50)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    turno = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# -----------------------------
#        MODELO CITA
# -----------------------------
class CitaDental(models.Model):
    paciente = models.ForeignKey(PacienteDental, on_delete=models.CASCADE)
    odontologo = models.ForeignKey(Odontologo, on_delete=models.CASCADE)
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    motivo_cita = models.TextField()
    estado_cita = models.CharField(max_length=50)
    comentarios = models.TextField(blank=True, null=True)
    tipo_tratamiento = models.CharField(max_length=100)

    def __str__(self):
        return f"Cita {self.id} - {self.fecha_cita}"


# -----------------------------
#      MODELO TRATAMIENTO
# -----------------------------
class TratamientoDental(models.Model):
    nombre_tratamiento = models.CharField(max_length=100)
    descripcion = models.TextField()
    costo_promedio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_estimada_minutos = models.IntegerField()
    es_invasivo = models.BooleanField()
    requiere_anestesia = models.BooleanField()
    materiales_comunes = models.TextField()

    def __str__(self):
        return self.nombre_tratamiento


# -----------------------------
#   MODELO HISTORIAL TRATAMIENTO
# -----------------------------
class HistorialTratamiento(models.Model):
    cita = models.ForeignKey(CitaDental, on_delete=models.CASCADE)
    paciente = models.ForeignKey(PacienteDental, on_delete=models.CASCADE)
    odontologo = models.ForeignKey(Odontologo, on_delete=models.CASCADE)
    tratamiento = models.ForeignKey(TratamientoDental, on_delete=models.CASCADE)
    fecha_realizacion = models.DateTimeField()
    notas_tratamiento = models.TextField()
    costo_final = models.DecimalField(max_digits=10, decimal_places=2)
    piezas_dentales_afectadas = models.TextField()

    def __str__(self):
        return f"Historial {self.id}"


# -----------------------------
#       MODELO FACTURA
# -----------------------------
class FacturaDental(models.Model):
    paciente = models.ForeignKey(PacienteDental, on_delete=models.CASCADE)
    fecha_emision = models.DateField()
    total_factura = models.DecimalField(max_digits=10, decimal_places=2)
    estado_pago = models.CharField(max_length=50)
    metodo_pago = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    cita_asociada = models.ForeignKey(CitaDental, on_delete=models.SET_NULL, null=True, blank=True)
    descuento_aplicado = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Factura {self.id}"


# -----------------------------
#   MODELO MATERIAL ODONTOLÓGICO
# -----------------------------
class MaterialOdontologico(models.Model):
    nombre_material = models.CharField(max_length=255)
    descripcion = models.TextField()
    stock_actual = models.IntegerField()
    fecha_caducidad = models.DateField()
    id_proveedor = models.IntegerField()  # No se definió modelo Proveedor
    costo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_material = models.CharField(max_length=50)
    ubicacion_almacen = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_material
