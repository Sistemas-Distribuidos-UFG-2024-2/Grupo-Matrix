import socket
import os

def servidor():
    server_port = int(os.getenv("SERVER_PORT", "5002"))  

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s4:
        s4.bind(('0.0.0.0', server_port))
        s4.listen()
        print(f"Servidor iniciado na porta {server_port} e aguardando conexões...")

        while True:
            conn, addr = s4.accept()  
            print(f"Conexão recebida de {addr}")

            with conn:
                data = conn.recv(1024)  
                if not data:  
                    print("Nenhum dado recebido. Encerrando a conexão.")
                    continue  
                
                print(f"Dados recebidos: {data.decode()}")
                conn.sendall(b'world!')  

if __name__ == "__main__":
    servidor()
