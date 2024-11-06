import socket
import threading
import random
import time

# Definição dos servidores e sua carga inicial
servidores = {
    'servidor1': ('127.0.0.1', 9001),
    'servidor2': ('127.0.0.1', 9002),
    'servidor3': ('127.0.0.1', 9003)
}

servidores_ativos = []

def verificar_servidores():
    global servidores_ativos
    while True:
        ativos = []
        for nome, (ip, porta) in servidores.items():
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(2)
                    s.connect((ip, porta))
                    ativos.append(nome)
            except (socket.timeout, socket.error):
                print(f"{nome} não está respondendo.")
        
        servidores_ativos = ativos
        print(f"Servidores ativos: {servidores_ativos}")
        time.sleep(5)

def balanceador():
    global servidores_ativos

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
        s2.bind(('0.0.0.0', 9000))
        s2.listen()
        print("Balanceador iniciado na porta 9000")

        while True:
            conn, addr = s2.accept()
            print(f"Conexão recebida de {addr}")

            with conn:
                data = conn.recv(1024)
                if not data:
                    print("Nenhum dado recebido. Encerrando a conexão.")
                    continue

                if not servidores_ativos:
                    conn.sendall('Erro: Nenhum servidor disponível.'.encode('utf-8'))
                    continue

                servidor_escolhido = random.choice(servidores_ativos)
                servidor_ip, servidor_porta = servidores[servidor_escolhido]

                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.connect((servidor_ip, servidor_porta))
                        s.sendall(data)
                        resposta = s.recv(1024)
                        conn.sendall(resposta)
                except socket.error as e:
                    print(f"Erro ao conectar ao {servidor_escolhido} ({servidor_ip}:{servidor_porta}): {e}")
                    conn.sendall('Erro ao conectar ao servidor.'.encode('utf-8'))

if __name__ == "__main__":
    # Inicia o thread que verifica os servidores
    threading.Thread(target=verificar_servidores, daemon=True).start()
    
    # Inicia o balanceador
    balanceador()
