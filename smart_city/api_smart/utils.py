import pandas as pd
from .models import Sensor, Ambiente, Historico
from django.http import HttpResponse




def importar_excel_sensor(req):
    # print(caminho_arquivo)
    arquivo_excel = req.FILES.get('file')
    
    if not arquivo_excel: 
        return HttpResponse("No file uploaded.", status=400)
    registros_importados = 0

    df = pd.read_excel(arquivo_excel)
    for _, row in df.iterrows():
        try:
            sensor = Sensor.objects.create(
                sensor=row['sensor'],
                mac_address=row['mac_address'],
                unidade_med=row['unidade_medida'],
                latitude=row['latitude'],
                longitude=row['longitude'],
                status=row['status'],
            )
            registros_importados += 1

        except Exception as e:
            print(f"[ERRO] Erro ao importar sensor: {e}")

    print(f"[INFO] {registros_importados} registros importados com sucesso.")
    return HttpResponse("tá ino")




def importar_excel_ambientes(req):
    df = pd.read_excel(req)
    registros_importados = 0

    for _, row in df.iterrows():
        try:
            ambiente = Ambiente.objects.get(id=row['ambiente'])
            sensor = Sensor.objects.get(id=row['sensor'])
            historico = Historico.objects.create(
                sensor=sensor,
                ambiente=ambiente,
                valor=row['valor'],
                timestamp=pd.to_datetime(row['timestamp'])  # conversão segura
            )
            registros_importados += 1

        except Exception as e:
            print(f"[ERRO] Erro ao importar histórico: {e}")

    print(f"[INFO] {registros_importados} registros importados com sucesso.")
    return f"{registros_importados} registros importados com sucesso."








def importar_excel_historico(req):
    arquivo_excel = req.FILES.get('file')
    
    if not arquivo_excel: 
        return HttpResponse("No file uploaded.", status=400)
    registros_importados = 0

    df = pd.read_excel(arquivo_excel)

    for _, row in df.iterrows():
        try:
            ambiente = Ambiente.objects.get(id=row['ambiente'])
            sensor = Sensor.objects.get(id=row['sensor'])
            historico = Historico.objects.create(
                sensor=sensor,
                valor=row['valor'],
                timestamp=pd.to_datetime(row['timestamp']),  # conversão segura
                ambiente=ambiente,
            )
            registros_importados += 1
        except Exception as e:
            print(f"[ERRO] Erro ao importar sensor: {e}")

    print(f"[INFO] {registros_importados} registros importados com sucesso.")
    return HttpResponse("tá ino")










