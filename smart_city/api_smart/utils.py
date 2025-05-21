import pandas as pd
from .models import Sensor, Ambiente, Historico

def importar_excel_temperatura(caminho_arquivo):
    df = pd.read_excel(caminho_arquivo)

    for _, row in df.iterrows():
        try:
            # Você pode identificar o ambiente com base em algum campo do Excel
            # Aqui, vamos supor que o DataFrame tenha a coluna 'ambiente_id'
            ambiente = Ambiente.objects.get(id=row['ambiente_id'])

            sensor = Sensor.objects.create(
                tipo=row['tipo'],  # Ex: 'temperatura'
                localizacao=row['localizacao'],  # Ex: 'Sala 01'
                status=row['status'],  # Ex: 'ativo'
                ambiente=ambiente
            )

            Historico.objects.create(
                sensor=sensor,
                valor=row['valor'],
                timestamp=row['timestamp']
            )

        except Sensor.DoesNotExist:
            print(f"Sensor de temperatura com ID {row['sensor']} não encontrado.")

