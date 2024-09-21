import socket
import threading
import time

servidores_ativos = []   # Lista dos servidores ativos (ip, porta)

def registrar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as verificador:
        verificador.bind(('127.0.0.1', 6000))  # Porta para servidores
        verificador.listen()
        print("Verificador aguardando registros de servidores...")

        while True:
            conn, addr = verificador.accept()
            with conn:
                servidor_info = conn.recv(1024).decode()  # Recebe IP e porta do servidor
                ip, porta = servidor_info.split(':')  # Extrai IP e porta
                servidores_ativos.append((ip, int(porta)))  # Adiciona o servidor na lista
                print(f"Servidor {ip}:{porta} registrado.")

def atender_balanceador():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as verificador:
        verificador.bind(('127.0.0.1', 6001))  # Porta para balanceador
        verificador.listen()
        print("Verificador aguardando conexões do balanceador...")

        while True:
            conn, addr = verificador.accept()
            with conn:
                if servidores_ativos: # Se tiver servidores na lista
                    for ip, porta in servidores_ativos:
                        try:
                            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                                s.settimeout(2) # Se não conseguir conectar ao servidor, lança socket.timeout
                                s.connect((ip, porta))
                                conn.sendall(f'{ip}:{porta}'.encode())  # Envia IP e porta ao balanceador
                                print(f"Verificador enviou {ip}:{porta} ao balanceador.")
                                break
                        except socket.error:
                            servidores_ativos.remove((ip, porta))  # Remove servidor inativo
                            print(f"Servidor {ip}:{porta} removido.")
                else:
                    conn.sendall(b'Nenhum servidor ativo.')

def iniciar_verificador():
    threading.Thread(target=registrar_servidor).start()  # Thread para registro de servidores
    threading.Thread(target=atender_balanceador).start()  # Thread para atender o balanceador

iniciar_verificador()
