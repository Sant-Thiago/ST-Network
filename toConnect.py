import subprocess
import os

def connect_to_wifi(ssid, password):
    try:
        # Comando para conectar-se à rede Wi-Fi
        command = f'nmcli dev wifi connect "{ssid}" password "{password}"'
        subprocess.call(["nmcli", "d", "wifi", "connect", ssid, "password", password])
        print(f'Conectando à rede {ssid}...')
        
        
    except subprocess.CalledProcessError as e:
        print(f'Erro ao conectar-se à rede Wi-Fi: {e}')

# Substitua 'YourSSID' e 'YourPassword' pelos valores corretos
connect_to_wifi('Jorge Henrique', 'Marilu2013')