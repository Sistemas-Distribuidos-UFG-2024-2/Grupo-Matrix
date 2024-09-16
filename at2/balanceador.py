import socket

def obter_servidor_ativo():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as balanceador:
        balanceador.connect(('127.0.0.1', 6001)) # Se conectar ao verificador de serviços
        ip = balanceador.recv(1024).decode()
        return ip

def balanceador():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 5000))
        s.listen()
        print("Balanceador aguardando conexão do cliente...")
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            print(f"Balanceador recebeu '{data.decode()}' de {addr[0]}:{addr[1]}")
            
            servidor_ip = obter_servidor_ativo()
            if servidor_ip != 'Nenhum servidor ativo.':
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
                   #Comunicação com o servidor
                    servidor.connect((servidor_ip, 5002))
                    servidor.sendall(data)
                    resposta = servidor.recv(1024)
                   
                   #Comunicação com o cliente 
                    conn.sendall(resposta)
                    print(f"Balanceador enviou resposta '{resposta.decode()}' de volta ao cliente.")
            else:
                print("Nenhum servidor ativo disponível.")

balanceador()
