import socket

def main():
    host = 'localhost'  # Endereço do middleware
    port = 5000         # Porta do middleware

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    nome = input("Digite o nome: ")
    sexo = input("Digite o sexo (masculino/feminino): ")
    idade = input("Digite a idade: ")

    metodo = "verificarMaioridade"  

    client_socket.sendall(metodo.encode())
    client_socket.sendall(b'\n')
    client_socket.sendall(nome.encode())
    client_socket.sendall(b'\n')
    client_socket.sendall(sexo.encode())
    client_socket.sendall(b'\n')
    client_socket.sendall(idade.encode())
    client_socket.sendall(b'\n')

    resposta = client_socket.recv(1024).decode()
    print("Resposta do servidor:", resposta)

    client_socket.close()

if __name__ == "__main__":
    main()
