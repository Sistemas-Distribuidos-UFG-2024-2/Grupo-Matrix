import socket
import threading
import time

servidores_ativos = [] # Lista dos servidores ativos

def registrar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as verificador:
        verificador.bind(('127.0.0.1', 6000)) # Porta para servidores
        verificador.listen()
        while True:
            conn, addr = verificador.accept()
            with conn:
                data = conn.recv(1024)
                if data.decode() == 'ativo': # Recebe a mensagem do servidor ativo
                    print(f"Servidor {addr[0]}:{addr[1]} registrou como ativo.")
                    servidores_ativos.append(addr[0]) # Adiciona o servidor na lista de servidores ativos

def verificar_servidor(ip):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)  #se o socket não conseguir estabelecer uma conexão, uma exceção socket.timeout será lançada
            s.connect((ip, 5002)) 
            return True
    except socket.error:
        return False

def atender_balanceador():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as verificador:
        verificador.bind(('127.0.0.1', 6001)) # Porta para balanceador
        verificador.listen()
        while True:
            conn, addr = verificador.accept()
            with conn:
                if servidores_ativos:
                    for ip in servidores_ativos: 
                        if verificar_servidor(ip): # Chama a função para verificar se está realemente ativo
                            conn.sendall(ip.encode()) # Se estiver ativo, envia para o balanceador
                            print(f"Verificador enviou o IP {ip} ao balanceador.")
                            break
                        else:
                            servidores_ativos.remove(ip) # Se não estiver ativo, remove o ip da lista
                            print(f"Servidor {ip} removido da lista.")
                else:
                    conn.sendall(b'Nenhum servidor ativo.')

def verificador_servicos():
    thread_registrar = threading.Thread(target=registrar_servidor)
    thread_balanceador = threading.Thread(target=atender_balanceador)

    thread_registrar.start()
    thread_balanceador.start()


verificador_servicos()
