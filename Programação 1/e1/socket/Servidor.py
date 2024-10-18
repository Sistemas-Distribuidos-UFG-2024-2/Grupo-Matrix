import socket

def calcular_reajuste(cargo, salario):
    if cargo.lower() == "operador":
        return salario * 1.20
    elif cargo.lower() == "programador":
        return salario * 1.18
    else:
        return salario

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 12345))
servidor.listen(1)

print("Servidor aguardando conexões...")

while True:
    conexao, endereco = servidor.accept()
    print(f"Conexão estabelecida com {endereco}")
    
    dados = conexao.recv(1024).decode('utf-8')
    nome, cargo, salario = dados.split(',')
    salario = float(salario)
    
    salario_reajustado = calcular_reajuste(cargo, salario)
    
    resposta = f"{nome}, seu salário reajustado é: {salario_reajustado:.2f}"
    conexao.send(resposta.encode('utf-8'))
    
    conexao.close()
