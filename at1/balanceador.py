import socket

def balanceador():
    s3_ip = '127.0.0.1'
    s3_port = 5001
    s4_ip = '127.0.0.1'
    s4_port = 5002

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
        s2.bind(('127.0.0.1', 5000))
        s2.listen()
        print("Balanceador aguardando conexão do cliente...")
        conn, addr = s2.accept()
        with conn:
            data = conn.recv(1024)
            print(f"Balanceador recebeu '{data.decode()}' de {addr[0]}:{addr[1]}")

            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s3:
                    s3.settimeout(2)
                    s3.connect((s3_ip, s3_port))
                    print(f"Conectado ao servidor 1 {s3_ip}:{s3_port}")
            except socket.error:
                print(f"Falha ao conectar ao servidor 1 {s3_ip}:{s3_port}. Tentando com servidor 2...")
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s4:
                    s4.connect((s4_ip, s4_port))
                    print(f"Conectado ao servidor {s4_ip}:{s4_port}")
                    s4.sendall(data)
                    print(f"Balanceador enviou '{data.decode()}' para {s4_ip}:{s4_port}")
                    resposta = s4.recv(1024)
                    print(f"Balanceador recebeu '{resposta.decode()}' de {s4_ip}:{s4_port}")
                    conn.sendall(resposta)
                    print(f"Balanceador enviou '{resposta.decode()}' de volta para {addr[0]}:{addr[1]}")

if __name__ == "__main__":
    balanceador()
