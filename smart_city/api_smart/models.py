from django.db import models


class Ambiente(models.Model):
    sig = models.IntegerField(primary_key=True)  # Identificador único (PK)
    descricao = models.CharField(max_length=100)
    ni = models.CharField(max_length=50)
    responsavel = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descricao} ({self.sig})"


class Sensor(models.Model):


    sensor = models.CharField(max_length=50)  # Nome ou código do sensor
    mac_address = models.CharField(max_length=50)
    unidade_med = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.CharField(max_length=10, choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')])

    def __str__(self):
        return f"{self.tipo} - {self.latitude}"


class Historico(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='historicos')
    valor = models.FloatField()
    timestamp = models.DateTimeField()  # melhor que IntegerField para data/hora
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE, related_name='historicos')

    def __str__(self):
        return f"{self.sensor.sensor} - {self.valor} em {self.timestamp.strftime('%d/%m/%Y %H:%M')}"
