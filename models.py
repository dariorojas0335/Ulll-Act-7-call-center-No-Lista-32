from django.db import models


class AgenteCallCenter(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    turno = models.CharField(max_length=50)
    habilidades_idiomas = models.TextField()
    estado_agente = models.CharField(max_length=50)
    dni = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class ClienteCallCenter(models.Model):
    nombre_empresa = models.CharField(max_length=255)
    contacto_principal = models.CharField(max_length=100)
    email_contacto = models.EmailField(max_length=100)
    telefono_contacto = models.CharField(max_length=20)
    sector = models.CharField(max_length=100)
    fecha_registro = models.DateField()
    historial_problemas = models.TextField()
    nivel_satisfaccion = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.nombre_empresa


class Llamada(models.Model):
    agente = models.ForeignKey(AgenteCallCenter, on_delete=models.CASCADE)
    cliente = models.ForeignKey(ClienteCallCenter, on_delete=models.CASCADE)
    fecha_hora_inicio = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField()
    duracion_segundos = models.IntegerField()
    tipo_llamada = models.CharField(max_length=50)
    resultado_llamada = models.CharField(max_length=50)
    grabacion_url = models.CharField(max_length=255)
    motivo_llamada = models.TextField()
    calificacion_cliente = models.IntegerField()

    def __str__(self):
        return f"Llamada {self.id}"


class ProblemaReportado(models.Model):
    llamada = models.ForeignKey(Llamada, on_delete=models.CASCADE)
    descripcion_problema = models.TextField()
    estado_problema = models.CharField(max_length=50)
    fecha_resolucion_estimada = models.DateField()
    prioridad = models.CharField(max_length=20)
    agente_resolvio = models.ForeignKey(AgenteCallCenter, on_delete=models.SET_NULL, null=True)
    tipo_problema = models.CharField(max_length=50)
    comentarios_resolucion = models.TextField()

    def __str__(self):
        return f"Problema {self.id}"


class EncuestaSatisfaccion(models.Model):
    llamada = models.ForeignKey(Llamada, on_delete=models.CASCADE)
    fecha_encuesta = models.DateTimeField()
    calificacion_general = models.IntegerField()
    calificacion_agente = models.IntegerField()
    comentarios = models.TextField()
    fecha_envio_encuesta = models.DateTimeField()
    fue_completada = models.BooleanField()

    def __str__(self):
        return f"Encuesta {self.id}"


class Campana(models.Model):
    nombre_campana = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    tipo_campana = models.CharField(max_length=50)
    objetivo = models.TextField()
    publico_objetivo = models.TextField()
    presupuesto_campana = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_campana


class ParticipacionCampana(models.Model):
    agente = models.ForeignKey(AgenteCallCenter, on_delete=models.CASCADE)
    campana = models.ForeignKey(Campana, on_delete=models.CASCADE)
    fecha_inicio_participacion = models.DateField()
    fecha_fin_participacion = models.DateField()
    num_llamadas_realizadas = models.IntegerField()
    num_exitos = models.IntegerField()
    tiempo_promedio_llamada = models.IntegerField()

    def __str__(self):
        return f"Participación {self.id}"
