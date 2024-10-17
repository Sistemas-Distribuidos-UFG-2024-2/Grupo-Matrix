import socket

# Função para verificar se o funcionário pode se aposentar
def verificar_aposentadoria(idade, tempo_servico):
    if idade >= 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25):
        return "O funcionário pode se aposentar."
    else:
        return "O funcionário NÃO pode se aposentar."

# Função principal do servidor
def main():
    host = 'localhost'  # Endereço do servidor
    port = 5001         # Porta de comunicação

    # Criar socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    # Escutar conexões
    server_socket.listen(5)
    print(f"Servidor de Aposentadoria está rodando na porta {port}...")

    while True:
        # Aceitar conexão
        client_socket, addr = server_socket.accept()
        print(f"Conexão estabelecida com: {addr}")

        # Receber dados do cliente
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        # Dividir os dados recebidos (idade e tempo de serviço)
        idade, tempo_servico = map(int, data.split(","))
        
        # Verificar aposentadoria
        resultado = verificar_aposentadoria(idade, tempo_servico)

        # Enviar resposta para o cliente
        client_socket.send(resultado.encode('utf-8'))

        # Fechar conexão com o cliente
        client_socket.close()

if __name__ == "__main__":
    main()
