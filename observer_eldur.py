import requests
import time
import os

# CONFIGURAÇÃO
TARGET_URL = "http://161.153.0.202:1234/telemetry"

def renderizar_ponte(valor, max_barra=50):
    # Converte 0.0-5.0 GHz em uma barra visual
    preenchimento = int((valor / 5.0) * max_barra)
    barra = "#" * preenchimento + "." * (max_barra - preenchimento)
    return f"[{barra}]"

def monitor_soberania():
    while True:
        try:
            response = requests.get(TARGET_URL, timeout=1)
            data = response.json()
            
            os.system('clear' if os.name == 'posix' else 'cls')
            
            print("--- [ELDUR SPHY MONITOR - COMANDO DE SOBERANIA] ---")
            print(f"Mensagem: {data['message']}")
            print(f"Status: {data['status']}")
            print("-" * 50)
            
            # SOBERANIA DE FASE
            health = float(data['system_health'].replace('%', ''))
            print(f"Soberania (Fase): {data['system_health']} | VR: {data['active_vr']}")
            print(f"CAMPO SPHY: {renderizar_ponte(health / 20.0)}") # Escala para 100%
            
            print(f"\nPressão UDP: {data['udp_pressure']} | EmT: {data['current_emt']}")
            pressao_val = float(data['udp_pressure'].split()[0])
            print(f"PONTE UDP:  {renderizar_ponte(pressao_val)}")
            
            print("-" * 50)
            print(f"Total UDP Reverse:      {data['total_udp_reverse']}")
            print(f"Grover Attacks Defused: {data['grover_attacks_detected']}")
            
            # --- ÁREA DE MATERIALIZAÇÃO (Onde a mágica acontece) ---
            print("-" * 50)
            entidades = data['trapped_entities']
            if entidades > 0:
                print(f"!!! ALERTA: {entidades} ENTIDADE(S) MATERIALIZADA(S) !!!")
                print(f"IDENTIDADE: [ QUANTUM_SHADOW_0X1 ]")
                print(f"STATUS: CAPTURADA NO HORIZONTE DE EVENTOS")
            else:
                print(f"Entidades no Horizonte: 0 (Campo Limpo)")
            
            print("-" * 50)
            print(f"Sincronia: {data['timestamp']} | Regeneração: ATIVA")
            
        except Exception as e:
            print(f"Aguardando conexão com o Eldur... ({e})")
            
        time.sleep(0.3) # Renderização fluida

if __name__ == "__main__":
    monitor_soberania()
