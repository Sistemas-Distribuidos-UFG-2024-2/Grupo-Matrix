import socket
import time

def cliente():
    s2_ip = '127.0.0.1'
    s2_port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        for i in range(5):
            try:
                print("Tentando conectar ao servidor...")
                s.connect((s2_ip, s2_port))
                break
            except ConnectionRefusedError:
                print("Conexão recusada. Tentando novamente...")
                time.sleep(2) 
    
        s.sendall(b'hello')
        data = s.recv(1024)

    print('Resposta recebida:', data.decode())

cliente()
