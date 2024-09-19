import socket
import threading
import time

ip_servidor = '127.0.0.1'
porta_servidor = 5002  

def notificar_verificador_de_servicos():
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
            try:
                servidor.connect(('127.0.0.1', 6000))  
                mensagem = f'{ip_servidor}:{porta_servidor}'  # Envia IP e porta para o verificador
                servidor.sendall(mensagem.encode())  
            except ConnectionRefusedError:
                print("Não foi possível conectar ao verificador de serviços.")
            time.sleep(5)  # Notifica o verificador a cada 5 segundos

def servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ip_servidor, porta_servidor)) 
        s.listen()
        print(f"Servidor aguardando conexões em {ip_servidor}:{porta_servidor}...")
        while True:
            conn, addr = s.accept() 
            threading.Thread(target=conectar_balanceador, args=(conn, addr)).start()

def conectar_balanceador(conn, addr):
    with conn:
        data = conn.recv(1024)  
        if data:
            print(f"Servidor {porta_servidor} recebeu '{data.decode()}' de {addr[0]}:{addr[1]}")
            conn.sendall(b'world!')  # Envia resposta ao cliente
            print(f"Servidor {porta_servidor} enviou 'world!' para {addr[0]}:{addr[1]}")

threading.Thread(target=notificar_verificador_de_servicos).start()
servidor()
