from django.db import models

class Ambiente(models.Model):
    nome = models.CharField(max_length=100)
    sig = models.CharField(max_length=10, unique=True)  # código identificador

    def __str__(self):
        return f"{self.nome} ({self.sig})"

class Sensor(models.Model):
    TIPOS = [
        ('temperatura', 'Temperatura'),
        ('umidade', 'Umidade'),
        ('luminosidade', 'Luminosidade'),
        ('contador', 'Contador'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPOS)
    localizacao = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')])
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE, related_name='sensores')

    def __str__(self):
        return f"{self.tipo} - {self.localizacao}"

class Historico(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='historicos')
    valor = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.sensor.tipo} - {self.valor} em {self.timestamp.strftime('%d/%m/%Y %H:%M')}"
