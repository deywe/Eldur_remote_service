import requests
import concurrent.futures

TARGET_IP = "161.153.0.202"
PORT = "1234"
URL = f"http://{TARGET_IP}:{PORT}/status"

def disparar_onda():
    try:
        requests.get(URL, timeout=1)
    except:
        pass

print(f"--- [PHASE SHIFT] Bombardeando Horizonte de Eventos em {TARGET_IP} ---")
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    # Dispara 100 sondagens rápidas
    for _ in range(100):
        executor.submit(disparar_onda)

print("Onda de choque finalizada. Verifique o tail -f no servidor.")
