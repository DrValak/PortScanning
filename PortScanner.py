# PORT SCANNING

import socket # Biblioteca para operações de rede
import sys # Biblioteca para manipulação do sistema
import threading # Biblioteca para operações de threading
import logging # Biblioteca para logging profissional
import json # Biblioteca para manipulação de JSON
import argparse # Biblioteca para argumentos de linha de comando
import os # Biblioteca para operações do sistema operacional
from pathlib import Path # Biblioteca para manipulação de caminhos
from datetime import datetime # Biblioteca para manipulação de datas
from concurrent.futures import ThreadPoolExecutor # Biblioteca para execução de tarefas em paralelo

# Configuração do sistema de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('port_scanner.log'),  # Salva em arquivo
        logging.StreamHandler()  # Mostra no terminal
    ]
)

logger = logging.getLogger(__name__)

def load_config(config_file='config.json'):
    """
    Carrega configurações do arquivo JSON.
    Retorna dicionário com as configurações.
    """
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
            logger.info(f"Configurações carregadas de {config_file}")
            return config
    except FileNotFoundError:
        logger.warning(f"Arquivo {config_file} não encontrado. Usando configurações padrão.")
        return {
            "scan_settings": {
                "default_timeout": 1,
                "max_threads": 100,
                "default_start_port": 1,
                "default_end_port": 100
            },
            "common_ports": [80, 443, 22, 21, 25, 53, 110, 143],
            "logging": {"enabled": True, "log_file": "port_scanner.log"},
            "output": {"save_results": False}
        }
    except json.JSONDecodeError as e:
        logger.error(f"Erro ao ler config.json: {e}")
        sys.exit(1)

def save_results(scan_data, output_dir='scan_results', config=None):
    """
    Salva resultados do scan em arquivo JSON com informações profissionais.
    """
    try:
        # Cria diretório se não existir
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Adiciona informações de negócio ao relatório se configurado
        if config and config.get('output', {}).get('include_business_header', False):
            business_info = config.get('business_info', {})
            scan_data['report_header'] = {
                'company_name': business_info.get('company_name', ''),
                'consultant_name': business_info.get('consultant_name', ''),
                'contact_email': business_info.get('email', ''),
                'contact_phone': business_info.get('phone', ''),
                'website': business_info.get('website', ''),
                'license_number': business_info.get('license_number', '')
            }
        
        # Nome do arquivo com timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{output_dir}/scan_{scan_data['target']}_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(scan_data, f, indent=2)
        
        logger.info(f"✅ Resultados salvos em: {filename}")
        return filename
    except Exception as e:
        logger.error(f"❌ Erro ao salvar resultados: {e}")
        return None

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
        logger.error("Erro ao obter o IP local.")
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
        logger.error(f"Erro: O host {target} não pôde ser resolvido.")
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
            
            logger.info(f"Porta {port} - Aberta ({service})")
            return True
        else:
            return False
            
    except socket.gaierror:
        logger.error(f"Erro: O host {target} não pôde ser resolvido.")
        return False
    except socket.error:
        return False
    finally:
        s.close()


def scan_ports(target, start_port, end_port, max_threads=100, client_name=None, project_name=None):
    """
    Escaneia um intervalo de portas usando multi-threading.
    Retorna dicionário com resultados do scan.
    """
    total_ports = end_port - start_port + 1
    completed = [0]  # Usa lista para compartilhar entre threads
    open_ports = []  # Lista de portas abertas
    lock = threading.Lock()  # Previne conflitos
    
    def scan_with_progress(port):
        result = port_scan(target, port)
        
        # Atualiza progresso de forma segura
        with lock:
            completed[0] += 1
            progress = (completed[0] / total_ports) * 100
            
            # Se porta aberta, adiciona à lista
            if result:
                try:
                    service = socket.getservbyport(port)
                except OSError:
                    service = "Serviço Desconhecido"
                open_ports.append({"port": port, "service": service})
            
            # Mostra progresso a cada 10 portas
            if completed[0] % 10 == 0 or completed[0] == total_ports:
                bar_length = 20
                filled = int(bar_length * completed[0] / total_ports)
                bar = '█' * filled + '░' * (bar_length - filled)
                print(f"\rProgresso: [{bar}] {progress:.0f}% ({completed[0]}/{total_ports})", end='')
        
        return result
    
    logger.info(f"Iniciando scan de {total_ports} portas em {target}")
    start_time = datetime.now()
    
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(scan_with_progress, port) 
                   for port in range(start_port, end_port + 1)]
        
        for future in futures:
            future.result()
    
    print()  # Nova linha após barra de progresso
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    logger.info(f"Escaneamento concluído em {duration:.2f} segundos!")
    logger.info(f"Portas abertas encontradas: {len(open_ports)}")
    
    # Retorna resultados estruturados
    results = {
        "target": target,
        "start_port": start_port,
        "end_port": end_port,
        "total_ports_scanned": total_ports,
        "open_ports": open_ports,
        "scan_duration_seconds": duration,
        "timestamp": datetime.now().isoformat(),
        "scanner_version": "2.0"
    }
    
    # Adiciona informações do cliente se fornecidas
    if client_name:
        results["client_name"] = client_name
    if project_name:
        results["project_name"] = project_name
    
    return results

if __name__ == "__main__":
    
    # Carrega configurações
    config = load_config()
    
    # Configura parser de argumentos de linha de comando
    parser = argparse.ArgumentParser(
        description='Port Scanner Enterprise - Ferramenta profissional de escaneamento de portas',
        epilog='Exemplo: python PortScanner.py -t 127.0.0.1 -p 1-1000 --save'
    )
    
    parser.add_argument('-t', '--target', 
                       help='Endereço IP ou hostname alvo')
    parser.add_argument('-p', '--ports', 
                       help='Intervalo de portas (ex: 1-100 ou 80,443,8080)')
    parser.add_argument('--common', action='store_true',
                       help='Escanear apenas portas comuns')
    parser.add_argument('--threads', type=int, 
                       default=config['scan_settings']['max_threads'],
                       help=f'Número de threads (padrão: {config["scan_settings"]["max_threads"]})')
    parser.add_argument('--save', action='store_true',
                       help='Salvar resultados em arquivo JSON')
    parser.add_argument('--timeout', type=int,
                       default=config['scan_settings']['default_timeout'],
                       help=f'Timeout por porta em segundos (padrão: {config["scan_settings"]["default_timeout"]})')
    parser.add_argument('--no-banner', action='store_true',
                       help='Não mostrar banner de IP local')
    parser.add_argument('--client', type=str,
                       help='Nome do cliente para o relatório')
    parser.add_argument('--project', type=str,
                       help='Nome do projeto/engajamento')
    
    args = parser.parse_args()
    
    # Mostra banner se não desabilitado
    if not args.no_banner:
        local_ip = get_local_ip()
        print("=" * 60)
        print(f"🛡️  PORT SCANNER ENTERPRISE v2.0")
        print(f"🖥️  Seu IP local: {local_ip}")
        print("=" * 60)
        print()
    
    # Determina target
    if args.target:
        target_host = args.target
    else:
        # Modo interativo
        print("💡 Dica: Use --help para ver todas as opções de linha de comando")
        print()
        target_host = input("Digite o endereço IP ou nome do host alvo: ")
    
    # Valida target
    if not validate_target(target_host):
        logger.error(f"❌ Host inválido: {target_host}")
        sys.exit(1)
    
    # Determina portas a escanear
    if args.common:
        # Escaneia portas comuns do config
        ports_to_scan = config['common_ports']
        logger.info(f"Escaneando {len(ports_to_scan)} portas comuns")
        
        # Cria resultado vazio
        all_results = {
            "target": target_host,
            "open_ports": [],
            "total_ports_scanned": len(ports_to_scan),
            "timestamp": datetime.now().isoformat(),
            "scanner_version": "2.0"
        }
        
        # Adiciona informações do cliente se fornecidas
        if args.client:
            all_results["client_name"] = args.client
        if args.project:
            all_results["project_name"] = args.project
        
        start_time = datetime.now()
        
        # Escaneia cada porta comum
        for port in ports_to_scan:
            if port_scan(target_host, port):
                try:
                    service = socket.getservbyport(port)
                except OSError:
                    service = "Serviço Desconhecido"
                all_results["open_ports"].append({"port": port, "service": service})
        
        end_time = datetime.now()
        all_results["scan_duration_seconds"] = (end_time - start_time).total_seconds()
        
        results = all_results
        
    elif args.ports:
        # Parse do formato de portas
        if '-' in args.ports:
            # Intervalo: 1-100
            start_port, end_port = map(int, args.ports.split('-'))
        elif ',' in args.ports:
            # Lista: 80,443,8080
            ports_list = list(map(int, args.ports.split(',')))
            start_port = min(ports_list)
            end_port = max(ports_list)
        else:
            # Porta única
            start_port = end_port = int(args.ports)
        
        print("-" * 60)
        print(f"🎯 Alvo: {target_host}")
        print(f"📊 Portas: {start_port} - {end_port}")
        print(f"🧵 Threads: {args.threads}")
        print("-" * 60)
        
        results = scan_ports(target_host, start_port, end_port, max_threads=args.threads,
                           client_name=args.client, project_name=args.project)
        
    else:
        # Modo interativo - pergunta intervalo
        start_port = input(f"Porta inicial (padrão {config['scan_settings']['default_start_port']}): ").strip()
        start_port = int(start_port) if start_port else config['scan_settings']['default_start_port']
        
        end_port = input(f"Porta final (padrão {config['scan_settings']['default_end_port']}): ").strip()
        end_port = int(end_port) if end_port else config['scan_settings']['default_end_port']
        
        print("-" * 60)
        print(f"🎯 Alvo: {target_host}")
        print(f"📊 Portas: {start_port} - {end_port}")
        print("-" * 60)
        
        results = scan_ports(target_host, start_port, end_port, max_threads=args.threads,
                           client_name=args.client, project_name=args.project)
    
    # Mostra resumo
    print()
    print("=" * 60)
    print(f"📋 RESUMO DO SCAN")
    print("=" * 60)
    if 'client_name' in results:
        print(f"Cliente: {results['client_name']}")
    if 'project_name' in results:
        print(f"Projeto: {results['project_name']}")
    print(f"Alvo: {results['target']}")
    print(f"Portas escaneadas: {results['total_ports_scanned']}")
    print(f"Portas abertas: {len(results['open_ports'])}")
    print(f"Tempo decorrido: {results['scan_duration_seconds']:.2f}s")
    
    if results['open_ports']:
        print(f"\n🔓 Portas abertas encontradas:")
        for item in results['open_ports']:
            print(f"   • Porta {item['port']:5d} - {item['service']}")
    else:
        print(f"\n🔒 Nenhuma porta aberta encontrada")
    
    print("=" * 60)
    
    # Salva resultados se solicitado
    if args.save or config['output']['save_results']:
        output_dir = config['output'].get('output_directory', 'scan_results')
        save_results(results, output_dir, config)
    
    logger.info("✅ Programa finalizado com sucesso!")
