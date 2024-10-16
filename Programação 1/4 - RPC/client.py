import grpc
import pesoideal_pb2
import pesoideal_pb2_grpc

def run():
    # Conectar ao servidor gRPC
    channel = grpc.insecure_channel('localhost:50051')
    stub = pesoideal_pb2_grpc.PesoIdealServiceStub(channel)

    # Coletar dados do usuário
    altura = float(input("Digite a altura: "))
    sexo = input("Digite o sexo (M/F): ").strip().upper()

    # Criar a requisição
    request = pesoideal_pb2.PesoIdealRequest(altura=altura, sexo=sexo)

    try:
        # Fazer a chamada RPC ao servidor
        response = stub.CalcularPesoIdeal(request)
        print(f"O peso ideal calculado é: {response.pesoIdeal:.2f} kg")
    except grpc.RpcError as e:
        print(f"Erro ao calcular o peso ideal: {e.details()}")

if __name__ == "__main__":
    run()
