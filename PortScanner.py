# PORT SCANNING

import socket # Biblioteca para operações de rede
import sys # Biblioteca para manipulação do sistema
from concurrent.futures import ThreadPoolExecutor # Biblioteca para execução de tarefas em paralelo


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
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        # Cria uma lista de tarefas para executar em paralelo
        futures = [executor.submit(port_scan, target, port) for port in range(start_port, end_port + 1)]
        
        # Aguarda todas as tarefas completarem
        for future in futures:
            future.result()


if __name__ == "__main__":
    
    target_host = input("Digite o endereço IP ou nome do host alvo: ")
    
    print("-" * 50)
    print(f"Escaneando alvo: {target_host}")
    print("-" * 50)
    
    # Usa multi-threading para escanear as portas
    scan_ports(target_host, 1, 100, max_threads=100)
    
    print("-" * 50)
    print("Escaneamento concluído!")
    print("-" * 50)
