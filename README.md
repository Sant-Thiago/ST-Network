# ST-Network

Este repositório contém uma aplicação em Python para listar redes Wi-Fi disponíveis, conectar-se a redes Wi-Fi e quebrar senhas de redes Wi-Fi.

## Estrutura do Projeto

- **Python**: Implementa todas as funcionalidades principais, desde a listagem das redes Wi-Fi até a quebra de senhas.

## Arquivos do Projeto

- **`app.py`**: Código principal que instancia e utiliza a classe `Network` para realizar as operações de rede.
- **`network.py`**: Implementação das funções para listar, conectar e quebrar senhas de redes Wi-Fi.

## Funcionalidades Principais

1. **Listar Redes Wi-Fi**:
   - **Listar Redes Disponíveis**: Mostra todas as redes Wi-Fi disponíveis nas proximidades.

2. **Conectar a Redes Wi-Fi**:
   - **Conectar a uma Rede Específica**: Permite conectar-se a uma rede Wi-Fi especificando o SSID e a senha.

3. **Quebrar Senhas de Wi-Fi**:
   - **Quebrar Senha de uma Rede Wi-Fi**: Tenta quebrar a senha de uma rede Wi-Fi utilizando uma geração aleatória de senhas.

## Como Executar o Projeto

1. **Instalar Dependências**:
   - Certifique-se de ter o Python instalado em seu sistema.

2. **Configurar e Executar o Projeto**:
   - Clone o repositório:
     ```sh
     git clone https://github.com/Sant-Thiago/ST-Network.git
     cd ST-Network
     ```
   - Execute o script `app.py` para utilizar as funcionalidades da ferramenta:
     ```sh
     python app.py
     ```

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para implementar todas as funcionalidades.
- **subprocess**: Módulo Python usado para executar comandos do sistema.
- **os**: Módulo Python utilizado para interações com o sistema de arquivos.

## Contribuição

Contribuições são bem-vindas! Para sugestões ou problemas encontrados, abra uma issue neste repositório.

---

Desenvolvido por [Sant-Thiago](https://github.com/Sant-Thiago/)
