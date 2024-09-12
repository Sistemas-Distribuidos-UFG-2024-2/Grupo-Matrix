import socket

def servidor_s4():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s4:
        s4.bind(('127.0.0.1', 5002))
        s4.listen()
        conn, addr = s4.accept()
        with conn:
            data = conn.recv(1024)
            conn.sendall(b'world!')

if __name__ == "__main__":
    servidor_s4()
