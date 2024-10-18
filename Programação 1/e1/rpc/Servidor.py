from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

# Função remota que calcula o reajuste salarial
def calcular_reajuste(nome, cargo, salario):
    if cargo.lower() == "operador":
        salario_reajustado = salario * 1.20
    elif cargo.lower() == "programador":
        salario_reajustado = salario * 1.18
    else:
        salario_reajustado = salario

    return f"{nome}, seu salário reajustado é: {salario_reajustado:.2f}"

server = SimpleJSONRPCServer(("localhost", 8000))
print("Servidor JSON-RPC rodando na porta 8000...")

server.register_function(calcular_reajuste, "calcular_reajuste")

server.serve_forever()
