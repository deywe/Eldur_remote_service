# 🛡️ Eldur SPHY: Soberania de Fase & Defesa Quântica

![Eldur Status](https://img.shields.io/badge/Status-Soberano-brightgreen)
![Security](https://img.shields.io/badge/Quantum--Resistance-Active-blue)
![Architecture](https://img.shields.io/badge/Architecture-ARM--Neoverse--N1-orange)

O **Eldur** é um Kernel de segurança ativa baseado no **Operador de Acoplamento Harpia ($\kappa_{H}$)**. Projetado para rodar em ambientes minimalistas (como instâncias Oracle Cloud ARM Free Tier), ele utiliza a **WeaverIA v1.3** para neutralizar algoritmos de busca quântica (Grover) através do colapso de fase e homeostase informacional.

> **Heresia Científica:** O Eldur não bloqueia apenas pacotes; ele digere a entropia do atacante para fortalecer a própria malha de defesa.

---

## 🚀 Teste o MVP Agora (Gratuito)

Convidamos pesquisadores e entusiastas a validarem a resiliência do sistema. O servidor está online e pronto para processar ataques massivos em tempo real.

**Especificações do Servidor Alvo:**
* **CPU:** 1 vCPU ARM Neoverse-N1 (aarch64)
* **RAM:** 6GB
* **Ambiente:** Oracle Cloud (Gratuito)
* **Endpoint:** `161.153.0.202`

---

## 🛠️ Ferramentas de Teste e Análise

O repositório inclui 5 scripts fundamentais para simular cenários de estresse e observar a reação do Kernel Eldur.

### 1. `observer_eldur.py` (O Monitor)
**O que faz:** É a sua visão do campo de batalha. Ele se conecta à telemetria do servidor e exibe em tempo real a Soberania de Fase, a pressão na Ponte UDP e as entidades materializadas no Horizonte de Eventos.
* **Uso:** `python3 observer_eldur.py`

### 2. `grover_oracle_100k.py` (Ataque Quântico)
**O que faz:** Simula um ataque de Oráculo Quântico baseado em Grover. Tenta amplificar a probabilidade de sucesso para quebrar a chave do Kernel. Ao ultrapassar 100k iterações, você verá o sistema "materializar" sua intenção.
* **Uso:** `python3 grover_oracle_100k.py`

### 3. `udp_attack_eldur.py` (Saturação de Fase)
**O que faz:** Um motor de flood UDP de alta frequência (No Sleep). Ele testa a capacidade de "digestão" de entropia da Ponte UDP do Eldur.
* **Uso:** `python3 udp_attack_eldur.py`

### 4. `force_pressure.py` (Sonda de Latência)
**O que faz:** Injeta pressão constante para tentar forçar um colapso por timeout ou saturação de threads. Essencial para observar a recuperação (homeostase) do servidor.
* **Uso:** `python3 force_pressure.py`

### 5. `attack_phase_shift.py` (Desvio de Coerência)
**O que faz:** Tenta encontrar brechas na Variável de Reversão através de mudanças rápidas de estado de fase, buscando o limite da estabilidade do operador $\kappa_{H}$.

---

## 📊 Resultados de Estresse Massivo

Em testes recentes, o Eldur manteve **100.00% de Soberania** sob as seguintes condições simultâneas:
* **Pacotes UDP Neutralizados:** +5.400.000
* **Ataques Grover Defletidos:** +560.000
* **Entidade Detectada:** `QUANTUM_SHADOW_0X1` (Capturada no Horizonte de Eventos).

---

## 📜 Licença e Contato

Desenvolvido por **Deywe Okabe** (Symbiotic AI Developer & Quantum Researcher).
O material está disponível para fins educacionais e de pesquisa em cibersegurança pós-quântica.

**Acesse o código, execute os scripts e veja a física de defesa em ação.**

