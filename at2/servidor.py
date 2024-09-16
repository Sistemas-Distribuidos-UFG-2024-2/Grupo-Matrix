import socket

def notificar_verificador_de_servicos():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.connect(('127.0.0.1', 6000))
        servidor.sendall(b'ativo')

def servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 5002))
        s.listen()
        print("Servidor aguardando conexão...")
        conn, addr = s4.accept()
        with conn:
            data = conn.recv(1024)
            print(f"Servidor recebeu '{data.decode()}' de {addr[0]}:{addr[1]}")
            conn.sendall(b'world!')
            print(f"Servidor enviou 'world!' para {addr[0]}:{addr[1]}")

notificar_verificador_de_servicos()
servidor()
