# 🐍 Simple Port Scanner (TCP)

## 📖 Introdução

Este projeto é um **Port Scanner (Scanner de Portas)** básico desenvolvido em Python. Seu objetivo é identificar quais portas TCP estão abertas em um host específico, sendo uma ferramenta essencial na fase inicial de **reconhecimento** em um teste de penetração ou análise de segurança.

O script foi criado para praticar o uso da biblioteca `socket` do Python, tratamento de exceções e manipulação de fluxos de rede.

## ✨ Funcionalidades

* **Varredura TCP:** Utiliza a função `connect_ex` da biblioteca `socket` para testar a conectividade TCP, simulando o início do *Three-Way Handshake*.
* **Timeout Definido:** Possui um *timeout* de 1 segundo para garantir a rapidez da varredura, evitando bloqueios em portas filtradas ou fechadas.
* **Portas Comuns:** Por padrão, escaneia o intervalo das 100 portas mais comuns (1 a 100).
* **Identificação de Serviço:** Tenta identificar o nome do serviço padrão associado a cada porta aberta (ex: porta 80 → `http`).

## 🛠️ Como Executar

### Pré-requisitos

* Python 3.x instalado.

### Execução

1.  **Clone o Repositório:**
    ```bash
    git clone [LINK_DO_SEU_REPOSITORIO]
    cd simple-port-scanner
    ```

2.  **Execute o Script:**
    ```bash
    python port_scanner.py
    ```

3.  **Insira o Alvo:** O programa solicitará que você digite o endereço IP ou nome do host que deseja escanear.

    > **⚠️ Nota de Segurança:** Sempre obtenha permissão expressa (por escrito) antes de escanear qualquer rede ou sistema que não seja de sua propriedade.

## 💡 Próximos Passos e Oportunidades de Melhoria

Este é um projeto inicial robusto. Para evoluir esta ferramenta e aplicar os conceitos de POO e concorrência que discutimos, considere as seguintes melhorias:

1.  **Argumentos de Linha de Comando:** Utilizar `argparse` ou `Click` para receber o alvo (`-t <alvo>`) e o intervalo de portas (`-p <min>-<max>`) como argumentos.
2.  **Refatoração POO:** Envolver a lógica de varredura em uma classe `PortScanner` para encapsulamento, herança e melhor modularidade.
3.  **Varredura Multithread:** Implementar `threading` ou `asyncio` para escanear múltiplas portas simultaneamente, aumentando drasticamente a velocidade.
