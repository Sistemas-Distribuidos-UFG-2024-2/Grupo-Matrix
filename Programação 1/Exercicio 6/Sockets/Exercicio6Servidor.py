import socket

# Função para calcular o desconto baseado no nível e número de dependentes
def calcular_desconto(nivel, num_dependentes):
    if nivel == "A":
        if num_dependentes > 0:
            return 0.08  # 8% de desconto se tiver dependentes
        else:
            return 0.03  # 3% de desconto se não tiver dependentes
    elif nivel == "B":
        if num_dependentes > 0:
            return 0.10  # 10% de desconto se tiver dependentes
        else:
            return 0.05  # 5% de desconto se não tiver dependentes
    elif nivel == "C":
        if num_dependentes > 0:
            return 0.15  # 15% de desconto se tiver dependentes
        else:
            return 0.08  # 8% de desconto se não tiver dependentes
    elif nivel == "D":
        if num_dependentes > 0:
            return 0.17  # 17% de desconto se tiver dependentes
        else:
            return 0.10  # 10% de desconto se não tiver dependentes
    else:
        return 0  # Nível inválido, sem desconto

# Função para processar o salário
def processar_salario(nome, nivel, salario_bruto, num_dependentes):
    desconto = calcular_desconto(nivel, num_dependentes)
    salario_liquido = salario_bruto * (1 - desconto)
    return f"Nome: {nome}, Nivel: {nivel}, Salario Liquido: R${salario_liquido:.2f}"

# Configuração do servidor
def servidor():
    host = 'localhost'  # Endereço do servidor
    port = 65432        # Porta de comunicação

    # Criação do socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Servidor escutando em {host}:{port}...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Conexão estabelecida com {addr}")

        # Recebendo dados do cliente
        dados = conn.recv(1024).decode()
        nome, nivel, salario_bruto, num_dependentes = dados.split(",")

        # Processa os dados
        resposta = processar_salario(nome, nivel, float(salario_bruto), int(num_dependentes))

        # Enviando a resposta para o cliente
        conn.send(resposta.encode())

        # Fechar conexão com o cliente
        conn.close()

if __name__ == "__main__":
    servidor()
