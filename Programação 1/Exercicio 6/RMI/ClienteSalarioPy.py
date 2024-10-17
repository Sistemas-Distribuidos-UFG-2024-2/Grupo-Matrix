import socket

def main():
    # Definir o endereço do servidor e a porta do adaptador de socket
    host = "localhost"
    port = 5000
    
    # Conectar ao adaptador de socket Java
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Coletar os dados do funcionário via terminal
    nome = input("Digite o nome do funcionário: ")
    nivel = input("Digite o nível do funcionário (A, B, C ou D): ")
    salario_bruto = float(input("Digite o salário bruto do funcionário: "))
    dependentes = int(input("Digite o número de dependentes do funcionário: "))

    # Enviar os dados para o adaptador de socket Java, seguido por uma nova linha
    data = f"{nome},{nivel},{salario_bruto},{dependentes}\n"  # Adicionando \n
    client_socket.send(data.encode())

    # Receber a resposta do servidor
    resposta = client_socket.recv(2048).decode()
    print("Resposta do servidor:", resposta)

    # Fechar a conexão
    client_socket.close()

if __name__ == "__main__":
    main()
