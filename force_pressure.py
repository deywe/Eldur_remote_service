import requests
import time
import concurrent.futures

TARGET_IP = "161.153.0.202"
PORT = "1234"
# Usamos uma rota que não existe ou forçamos o processamento
URL = f"http://{TARGET_IP}:{PORT}/kernel" 

def disparar_pressao():
    try:
        # Enviamos headers pesados ou fazemos requisições em massa
        # para tentar elevar o process_time no servidor
        requests.get(URL, headers={"X-Quantum-Pressure": "MAX"}, timeout=5)
    except:
        pass

print(f"--- [PRESSURE TEST] Forçando Colapso em {TARGET_IP} ---")
with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    # Disparar 200 vezes para garantir que o middleware sinta a carga
    for _ in range(200):
        executor.submit(disparar_pressao)

print("Ataque de pressão finalizado. Olhe o Monitor agora!")
