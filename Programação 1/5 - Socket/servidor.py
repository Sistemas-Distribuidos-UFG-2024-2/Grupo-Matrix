import socket

def classificar_nadador(idade):
    if 5 <= idade <= 7:
        return "infantil A"
    elif 8 <= idade <= 10:
        return "infantil B"
    elif 11 <= idade <= 13:
        return "juvenil A"
    elif 14 <= idade <= 17:
        return "juvenil B"
    elif idade >= 18:
        return "adulto"
    else:
        return "Idade fora das categorias."

def servidor():
    # Cria o socket
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define o IP e a porta para escutar
    servidor_socket.bind(('localhost', 12345))
    
    # Habilita o servidor para aceitar conexões
    servidor_socket.listen(1)
    
    print("Servidor aguardando conexão...")

    while True:
        conexao, endereco = servidor_socket.accept()
        print(f"Conectado a {endereco}")
        
        # Recebe a idade do cliente
        idade_recebida = conexao.recv(1024).decode()
        
        try:
            idade = int(idade_recebida)
        except ValueError:
            conexao.send("Idade inválida!".encode())
            conexao.close()
            continue

        # Classifica o nadador com base na idade
        categoria = classificar_nadador(idade)
        
        # Envia a resposta de volta ao cliente
        conexao.send(categoria.encode())
        conexao.close()

if __name__ == "__main__":
    servidor()
