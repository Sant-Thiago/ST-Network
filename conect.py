import subprocess

def list_wifi_networks():
    try:
        # Executar o comando para listar redes Wi-Fi disponíveis
        result = subprocess.run(['netsh', 'wlan', 'show', 'network'], capture_output=True, text=True)
        print(result.stdout)
        
        # Processar a saída, se necessário
        networks = []
        for line in result.stdout.split('\n'):
            if "SSID" in line:
                networks.append(line.strip())
        
        print("Redes Wi-Fi disponíveis:")
        for network in networks:
            print(network)
            
    except subprocess.CalledProcessError as e:
        print(f'Erro ao listar redes Wi-Fi: {e}')

list_wifi_networks()

import subprocess

def connect_to_wifi(ssid, password):
    try:
        # Comando para conectar-se à rede Wi-Fi
        command = f'nmcli dev wifi connect "{ssid}" password "{password}"'
        subprocess.run(command, shell=True, check=True)
        print(f'Conectando à rede {ssid}...')
        
    except subprocess.CalledProcessError as e:
        print(f'Erro ao conectar-se à rede Wi-Fi: {e}')

# Substitua 'YourSSID' e 'YourPassword' pelos valores corretos
connect_to_wifi('YourSSID', 'YourPassword')