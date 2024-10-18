import socket

def main():
    nome = input("Digite o nome do funcionário: ")
    cargo = input("Digite o cargo do funcionário (operador/programador): ").strip().lower()
    salario = float(input("Digite o salário do funcionário: "))

    try:
        # Configura o socket para se conectar ao servidor Java
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('localhost', 12345))
            
            # Envia cargo e salário para o servidor
            s.sendall(f"{cargo}\n".encode('utf-8'))
            s.sendall(f"{salario}\n".encode('utf-8'))

            # Recebe o salário reajustado do servidor
            data = s.recv(1024)
            salario_reajustado = float(data.decode('utf-8'))

            print(f"O salário reajustado de {nome} é: R$ {salario_reajustado:.2f}")
    except Exception as e:
        print("Erro ao se comunicar com o servidor:", e)

if __name__ == "__main__":
    main()
