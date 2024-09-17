import socket

ip_servidor = '127.0.0.1'
porta_servidor = 5002

def notificar_verificador_de_servicos():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.connect(('127.0.0.1', 6000))  
        mensagem = f'{ip_servidor}:{porta_servidor}' 
        servidor.sendall(mensagem.encode())  

def servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ip_servidor, porta_servidor)) 
        s.listen()
        print(f"Servidor aguardando conexão em {ip_servidor}:{porta_servidor}...")
        conn, addr = s.accept()  
        with conn:
            data = conn.recv(1024)  
            print(f"Servidor recebeu '{data.decode()}' de {addr[0]}:{addr[1]}")
            conn.sendall(b'world!')  
            print(f"Servidor enviou 'world!' para {addr[0]}:{addr[1]}")


notificar_verificador_de_servicos()
servidor()
