import socket

servidores = {
    'servidor1': ('servidor1', 5002),  # Nome do serviço Docker Compose e porta #ao rodar sem docker crie 3 arquivo servidor, mude para '127.0.0.1'
    'servidor2': ('servidor2', 5003),
    'servidor3': ('servidor3', 5004)
}

carga_servidores = {
    'servidor1': 0,
    'servidor2': 0,
    'servidor3': 0
}

def balanceador():
    ultimo_servidor_tentado = ''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
        s2.bind(('0.0.0.0', 5000))
        s2.listen()
        print("Balanceador iniciado na porta 5000")

        while True:
            conn, addr = s2.accept()
            print(f"Conexão recebida de {addr}")

            with conn:
                data = conn.recv(1024)
                if not data:
                    print("Nenhum dado recebido. Encerrando a conexão.")
                    continue

                count = 1

                # Fazendo loop nos servidores até que acabe os servidores ou encontre um disponível
                for i in servidores: 
                    if count == servidores.__len__:
                        conn.sendall(f'Erro: Nenhum servidor disponível.'.encode('utf-8'))
                        break

                    servidor = i
                    servidor_ip, servidor_porta = servidores[servidor]
                    try:
                        print(f"Tentando conectar ao {servidor} ({servidor_ip}:{servidor_porta})")
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                            s.connect((servidor_ip, servidor_porta))
                            s.sendall(data)
                            resposta = s.recv(1024)
                            conn.sendall(resposta)
                        
                        break
                    except socket.error as e:
                        print(f"Erro ao conectar ao {servidor} ({servidor_ip}:{servidor_porta}): {e}")
                        continue
                    finally:
                        count +=1
                    




if __name__ == "__main__":
    balanceador()
