# 🐍 Scanner de Portas Simples (TCP)

## 📖 Introdução

Este projeto consiste num **Scanner de Portas (Port Scanner)** básico desenvolvido em Python. A sua principal função é identificar quais as portas TCP estão ativas e abertas num alvo específico.

Trata-se de uma ferramenta fundamental na fase de **reconhecimento** (levantamento de informações) de qualquer análise ou teste de segurança. O script foi criado para praticar o uso da biblioteca `socket` do Python, tratamento de exceções e a gestão de recursos de rede.

## ✨ Funcionalidades

* **Varredura TCP:** Utiliza a função `connect_ex` da biblioteca `socket` para testar a conectividade TCP no alvo, simulando o início de um *handshake* de três vias. 
* **Timeout Definido:** Implementa um limite de tempo (*timeout*) de 1 segundo para garantir que a varredura seja rápida e eficiente, não ficando bloqueada em portas filtradas.
* **Portas Comuns:** Por predefinição, faz scan num intervalo das 100 portas mais frequentemente utilizadas (de 1 a 100).
* **Identificação de Serviço:** Tenta mapear o número da porta aberta para o nome do serviço padrão associado (ex: porta 22 → `ssh`).

## 🛠️ Como Executar

### Pré-requisitos

* Python 3.x instalado.

### Execução

1.  **Clonar o Repositório:**
    ```bash
    git clone [LINK_DO_SEU_REPOSITORIO]
    cd simple-port-scanner
    ```

2.  **Correr o Script:**
    ```bash
    python port_scanner.py
    ```

3.  **Inserir o Alvo:** O programa irá pedir que insira o endereço IP ou nome do host que pretende escanear.

    > **⚠️ Nota de Segurança:** É obrigatório obter sempre permissão explícita (por escrito) antes de fazer scan de qualquer rede ou sistema que não seja da sua propriedade.

## 💡 Próximos Passos e Oportunidades de Melhoria

Este é um projeto inicial sólido. Para continuar a evoluir a ferramenta e aplicar conceitos avançados de Python, considere as seguintes refatorações:

1.  **Argumentos de Linha de Comando:** Utilizar a biblioteca `argparse` para permitir que o alvo (`-t <alvo>`) e o intervalo de portas (`-p <min>-<max>`) sejam passados diretamente como argumentos ao correr o script.
2.  **Refatoração POO:** Reorganizar a lógica do scanner numa classe `PortScanner`, aplicando os conceitos de Programação Orientada a Objetos (POO) para maior modularidade e extensibilidade.
3.  **Varredura Concorrente:** Implementar `threading` ou `asyncio` para fazer scan de várias portas em simultâneo (concorrência), o que aumentará significativamente a velocidade de execução da ferramenta.
