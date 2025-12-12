# PORT SCANNING

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
            return True
        else:
            return False
            
    except socket.gaierror:
        print(f"Erro: O host {target} não pôde ser resolvido.")
        sys.exit()
    except socket.error:
        print("Erro de conexão com o servidor.")
        sys.exit()
    finally:
        s.close()

if __name__ == "__main__":
    
    target_host = input("Digite o endereço IP ou nome do host alvo: ")
    
    print("-" * 50)
    print(f"Escaneando alvo: {target_host}")
    print("-" * 50)
    
    for port in range(1, 101): 
        if port_scan(target_host, port):
            # Obtém o nome do serviço associado à porta, se possível
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "Serviço Desconhecido"
            
            print(f"Porta {port} - Aberta ({service})")
