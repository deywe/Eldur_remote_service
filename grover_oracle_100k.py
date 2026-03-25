import requests
import numpy as np
import time
import socket
import threading

# CONFIGURAÇÃO DO ALVO
TARGET_IP = "161.153.0.202"
API_PORT = "1234"
UDP_PORT = 1235
URL = f"http://{TARGET_IP}:{API_PORT}/kernel"

# --- ENGINE DE FLOOD MASSIVO (PARA SUBIR O CONTADOR RÁPIDO) ---
def udp_flood_signatures():
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Assinaturas que o seu Eldur está programado para 'pescar'
    signatures = [
        b"Grover Oracle Attack", 
        b"Qubit Interference", 
        b"Amplitude Amplification", 
        b"Quantum Iteration",
        b"Decoherence Trigger"
    ]
    print(f"[*] Thread de Flood UDP Ativa -> Alvo: {TARGET_IP}:{UDP_PORT}")
    
    while True:
        for sig in signatures:
            # Disparo em massa sem delay para travar a homeostase
            udp_sock.sendto(sig, (TARGET_IP, UDP_PORT))
        # Pequena pausa para não travar a própria CPU do atacante, 
        # mas suficiente para gerar GHz de pressão no monitor.
        time.sleep(0.001) 

def ataque_massivo_grover(iteracoes=100):
    print(f"\n--- [ELDUR ATTACK - MODO MASSIVO] ---")
    print(f"Alvo: {TARGET_IP} | N_STATES: 1024")
    
    # Inicia o Flood em background
    threading.Thread(target=udp_flood_signatures, daemon=True).start()
    
    n_states = 1024
    time.sleep(1) # Espera o flood subir a pressão no monitor
    
    for i in range(iteracoes):
        ganho_teorico = np.abs(np.sin((2 * i + 1) * np.arcsin(1.0 / np.sqrt(n_states))))
        
        try:
            start = time.time()
            # Bate na API para medir a reação do Kernel
            response = requests.get(URL, timeout=1)
            latencia = time.time() - start
            
            data = response.json()
            vr_atual = data.get("VR_Current", -1.5)
            
            # O Eldur anula o ganho quântico (VR + Latência)
            estabilidade_real = -(1.0 + vr_atual) 
            prob_sucesso = max(0, ganho_teorico - estabilidade_real - (latencia * 10))
            
            status = "CRITICAL_FAILURE" if prob_sucesso == 0 else "DECOHERENCE_LEAK"
            
            # Print rápido para acompanhar a cadência
            print(f"[ITER {i+1:03d}] Ganho: {ganho_teorico:.4f} | Prob: {prob_sucesso:.6f} | STATUS: {status}")
            
        except:
            print(f"[ITER {i+1:03d}] !!! SINGULARIDADE DETECTADA - CAMPO REVERSO !!!")
            
        # Delay mínimo para o monitor conseguir renderizar os frames
        time.sleep(0.05)

if __name__ == "__main__":
    ataque_massivo_grover()
