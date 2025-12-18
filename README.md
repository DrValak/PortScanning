# 🐍 Scanner de Portas Simples (TCP)

## 📖 Introdução

Este projeto consiste num **Scanner de Portas (Port Scanner)** desenvolvido em Python com suporte a **multi-threading** para varreduras rápidas e eficientes.  A sua principal função é identificar quais as portas TCP estão ativas e abertas num alvo específico. 

Trata-se de uma ferramenta fundamental na fase de **reconhecimento** (levantamento de informações) de qualquer análise ou teste de segurança.  O script foi criado para praticar o uso das bibliotecas `socket` e `concurrent.futures` em Python.

## ✨ Funcionalidades

* **Varredura TCP:** Utiliza a função `connect_ex` da biblioteca `socket` para testar a conectividade TCP no alvo, simulando o início de um *handshake* de três vias.  
* **Timeout Definido:** Implementa um limite de tempo (*timeout*) de 1 segundo para garantir que a varredura seja rápida e eficiente, não ficando bloqueada em portas filtradas.
* **Portas Comuns:** Por predefinição, faz scan num intervalo das 100 portas mais frequentemente utilizadas (de 1 a 100).
* **Identificação de Serviço:** Tenta mapear o número da porta aberta para o nome do serviço padrão associado (ex: porta 22 → `ssh`).
* **Varredura Concorrente:** Implementa `ThreadPoolExecutor` para fazer scan de várias portas em simultâneo, aumentando significativamente a velocidade de execução (até 100 threads em paralelo).
* **Código Modular:** Organizado com funções separadas (`port_scan` e `scan_ports`) para maior legibilidade e manutenção.

## 🛠️ Como Executar

### Pré-requisitos

* Python 3.x instalado. 

### Execução

1.   **Clonar o Repositório:**
    ```bash
    git clone https://github.com/DrValak/PortScanning.git
    cd PortScanning
    ```

2.  **Correr o Script:**
    ```bash
    python PortScanner. py
    ```

3.  **Inserir o Alvo:** O programa irá pedir que insira o endereço IP ou nome do host que pretende escanear.

    > **⚠️ Nota de Segurança:** É obrigatório obter sempre permissão explícita (por escrito) antes de fazer scan de qualquer rede ou sistema que não seja da sua propriedade.

## 📊 Exemplo de Utilização

```bash
$ python PortScanner.py
Digite o endereço IP ou nome do host alvo: scanme.nmap.org
--------------------------------------------------
Escaneando alvo:  scanme.nmap.org
--------------------------------------------------
Porta 22 - Aberta (ssh)
Porta 80 - Aberta (http)
--------------------------------------------------
Escaneamento concluído!
--------------------------------------------------
```

## 💡 Próximos Passos e Oportunidades de Melhoria

Este é um projeto funcional com varredura concorrente implementada.  Para continuar a evoluir a ferramenta e aplicar conceitos avançados de Python, considere as seguintes melhorias:

1.   **Argumentos de Linha de Comando:** Utilizar a biblioteca `argparse` para permitir que o alvo (`-t <alvo>`), o intervalo de portas (`-p <min>-<max>`) e o número de threads (`--threads <n>`) sejam passados diretamente como argumentos ao executar o script. 
2.  **Refatoração POO Completa:** Reorganizar a lógica do scanner numa classe `PortScanner`, aplicando completamente os conceitos de Programação Orientada a Objetos (POO) para maior modularidade e extensibilidade.
3.  **Exportação de Resultados:** Adicionar a capacidade de exportar os resultados do scan para ficheiros (JSON, CSV, XML) para análise posterior. 
4.  **Detecção de Versão de Serviço:** Implementar *banner grabbing* para tentar identificar a versão dos serviços em execução nas portas abertas.
5.  **Diferentes Tipos de Scan:** Adicionar suporte para outros tipos de varredura (SYN scan, UDP scan, etc.) utilizando bibliotecas como `scapy`.
6.  **Interface Gráfica:** Desenvolver uma GUI simples com `tkinter` ou `PyQt` para utilizadores menos familiarizados com a linha de comando. 
7.  **Logging:** Implementar um sistema de logging para registar todas as operações e resultados do scanner. 

## 📚 Tecnologias Utilizadas

- **Python 3.x**
- **socket** - Operações de rede
- **concurrent.futures** - Multi-threading para execução paralela
- **sys** - Manipulação do sistema

## 📄 Licença

Este projeto é distribuído sob licença livre para fins educacionais.  Use com responsabilidade e apenas em sistemas para os quais tem autorização. 
