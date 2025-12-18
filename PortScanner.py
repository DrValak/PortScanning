# PORT SCANNING

import socket # Biblioteca para operações de rede
import sys # Biblioteca para manipulação do sistema
import threading # Biblioteca para operações de threading
from concurrent.futures import ThreadPoolExecutor # Biblioteca para execução de tarefas em paralelo

def get_local_ip():
    """
    Obtém o endereço IP local da máquina.
    Retorna o IP como string.
    """
    try:
        # Cria um socket temporário para descobrir o IP local
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Conecta a um servidor externo (não envia dados)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "127.0.0.1"

def validate_target(target):
    """
    Valida se o alvo fornecido é um endereço IP ou nome de host válido.
    Retorna o endereço IP se válido, caso contrário, retorna None.
    """
    try:
        # Tenta resolver o nome do host para um endereço IP
        socket.gethostbyname(target)
        return target
    except socket.gaierror:
        print(f"Erro: O host {target} não pôde ser resolvido.")
        return None

def port_scan(target, port):
    """
    Tenta criar uma conexão TCP com a porta especificada no alvo.
    Retorna True se a porta estiver aberta, False caso contrário.
    """
    try:
        # Cria um objeto socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Define um timeout para que o programa não demore muito
        s.settimeout(1) 
        
        # Tenta conectar
        result = s.connect_ex((target, port))
        
        if result == 0:
            # Obtém o nome do serviço associado à porta, se possível
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "Serviço Desconhecido"
            
            print(f"Porta {port} - Aberta ({service})")
            return True
        else:
            return False
            
    except socket.gaierror:
        print(f"Erro: O host {target} não pôde ser resolvido.")
        return False
    except socket.error:
        return False
    finally:
        s.close()


def scan_ports(target, start_port, end_port, max_threads=100):
    """
    Escaneia um intervalo de portas usando multi-threading.
    """
    total_ports = end_port - start_port + 1
    completed = [0]  # Usa lista para compartilhar entre threads
    lock = threading.Lock()  # Previne conflitos
    
    def scan_with_progress(port):
        result = port_scan(target, port)
        
        # Atualiza progresso de forma segura
        with lock:
            completed[0] += 1
            progress = (completed[0] / total_ports) * 100
            
            # Mostra progresso a cada 10 portas
            if completed[0] % 10 == 0 or completed[0] == total_ports:
                bar_length = 20
                filled = int(bar_length * completed[0] / total_ports)
                bar = '█' * filled + '░' * (bar_length - filled)
                print(f"\rProgresso: [{bar}] {progress:.0f}% ({completed[0]}/{total_ports})", end='')
        
        return result
    
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(scan_with_progress, port) 
                   for port in range(start_port, end_port + 1)]
        
        for future in futures:
            future.result()
    
    print()  # Nova linha após a barra de progresso

if __name__ == "__main__":
    
    # Mostra o IP local do usuário
    local_ip = get_local_ip()
    print("=" * 50)
    print(f"🖥️  Seu IP local: {local_ip}")
    print("=" * 50)
    print()
    
    target_host = input("Digite o endereço IP ou nome do host alvo: ")
    
    print("-" * 50)
    print(f"Escaneando alvo: {target_host}")
    print("-" * 50)
    
    # Usa multi-threading para escanear as portas
    scan_ports(target_host, 1, 100, max_threads=100)
    
    print("-" * 50)
    print("Escaneamento concluído!")
    print("-" * 50)
