import socket

def main():
    # Conectar ao SocketAdapter Java
    HOST = 'localhost'  # O endereço IP do servidor
    PORT = 5000         # A porta onde o SocketAdapter está escutando

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # Leitura de dados do usuário
        idade = input("Digite a idade do funcionário: ")
        tempo_servico = input("Digite o tempo de serviço do funcionário: ")

        # Enviar dados para o servidor
        dados = f"{idade},{tempo_servico}\n"
        s.sendall(dados.encode())

        # Receber a resposta do servidor
        resposta = s.recv(1024).decode()
        print("Resposta do servidor:", resposta)

if __name__ == "__main__":
    main()
