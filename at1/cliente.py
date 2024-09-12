import socket

def cliente():
    s2_ip = '127.0.0.1'
    s2_port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((s2_ip, s2_port))
        s.sendall(b'hello')
        data = s.recv(1024)

    print('Resposta recebida:', data.decode())

if __name__ == "__main__":
    cliente()