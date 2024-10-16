import socket

# Função para calcular o peso ideal
def calcular_peso_ideal(altura, sexo):
    if sexo == 'M':
        return (72.7 * altura) - 58
    elif sexo == 'F':
        return (62.1 * altura) - 44.7
    else:
        return None

# Configurando o servidor
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432        # Porta usada pelo servidor

# Criando o socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Servidor aguardando conexão...")
    
    conn, addr = s.accept()
    with conn:
        print(f"Conectado a {addr}")
        
        # Recebendo dados do cliente
        data = conn.recv(1024).decode().strip()  # Recebe e decodifica
        
        if not data:
            print("Nenhum dado recebido")
        else:
            # Dividindo os dados recebidos (formato: altura,sexo)
            try:
                altura, sexo = data.split(',')
                altura = float(altura)
                sexo = sexo.strip().upper()

                # Calculando o peso ideal
                peso_ideal = calcular_peso_ideal(altura, sexo)
                
                # Enviando o resultado de volta ao cliente
                if peso_ideal is not None:
                    conn.sendall(f"{peso_ideal:.2f}".encode())
                else:
                    conn.sendall("Sexo inválido".encode())
            except Exception as e:
                conn.sendall(f"Erro ao processar os dados: {str(e)}".encode())
