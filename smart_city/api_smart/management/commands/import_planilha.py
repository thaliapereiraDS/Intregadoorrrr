from django.core.management.base import BaseCommand
import pandas as pd
from api_smart.models import Historico, Sensor
from django.utils.dateparse import parse_datetime
from ...utils import importar_excel_temperatura

class Command(BaseCommand):
    help = 'Importa dados de uma planilha Excel para o modelo Histórico'

    def add_arguments(self, parser):
        parser.add_argument('arquivo', type=str, help='Caminho da planilha .xlsx a ser importada')

    def handle(self, *args, **kwargs):
        caminho = kwargs['arquivo']
        df = pd.read_excel(caminho)

        for _, row in df.iterrows():
            try:
        
                Sensor.objects.create(
                    sensor=row['sensor'],
                    mac=row['valor'],
                    timestamp=parse_datetime(str(row['timestamp']))
                )
            except Sensor.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"Sensor ID {row['sensor']} não encontrado."))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Erro ao importar linha: {e}"))

        self.stdout.write(self.style.SUCCESS("Importação finalizada com sucesso!"))

