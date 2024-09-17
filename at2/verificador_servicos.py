import socket
import threading
import time

servidores_ativos = []  # Lista dos servidores ativos 

def registrar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as verificador:
        verificador.bind(('127.0.0.1', 6000))  # Porta para servidores
        verificador.listen()
        while True:
            conn, addr = verificador.accept()
            with conn:
                data = conn.recv(1024).decode()
                ip, porta = data.split(':')  # Recebe diretamente o IP e porta
                servidores_ativos.append((ip, int(porta)))  # Adiciona o servidor (IP, porta) à lista de servidores ativos
                print(f"Servidor {ip}:{porta} registrou como ativo.")
                
def verificar_servidor(ip, porta):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)  # Se o socket não conseguir estabelecer uma conexão, uma exceção socket.timeout será lançada
            s.connect((ip, porta))  # Usa a porta recebida do servidor
            return True
    except socket.error:
        return False

def atender_balanceador():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as verificador:
        verificador.bind(('127.0.0.1', 6001))  # Porta para balanceador
        verificador.listen()
        while True:
            conn, addr = verificador.accept()
            with conn:
                if servidores_ativos:
                    for ip, porta in servidores_ativos: 
                        if verificar_servidor(ip, porta):  # Chama a função para verificar se está realmente ativo
                            conn.sendall(f'{ip}:{porta}'.encode())  # Se estiver ativo, envia IP e porta para o balanceador
                            print(f"Verificador de serviços enviou o IP {ip}:{porta} ao balanceador.")
                            break
                        else:
                            servidores_ativos.remove((ip, porta))  # Se não estiver ativo, remove o IP e porta da lista
                            print(f"Servidor {ip}:{porta} removido da lista.")
                else:
                    conn.sendall(b'Nenhum servidor ativo.')

def verificador_servicos():
    thread_registrar = threading.Thread(target=registrar_servidor)
    thread_balanceador = threading.Thread(target=atender_balanceador)

    thread_registrar.start()
    thread_balanceador.start()


verificador_servicos()
