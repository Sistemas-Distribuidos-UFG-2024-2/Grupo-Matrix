from xmlrpc.server import SimpleXMLRPCServer

def verificar_maioridade(nome, sexo, idade):
    if sexo == "masculino" and idade >= 18:
        return f"{nome} já atingiu a maioridade."
    elif sexo == "feminino" and idade >= 21:
        return f"{nome} já atingiu a maioridade."
    else:
        return f"{nome} não atingiu a maioridade."

server = SimpleXMLRPCServer(("localhost", 1234))
print("Servidor Python aguardando conexões...")

server.register_function(verificar_maioridade, "VerificarMaioridade")

server.serve_forever()
