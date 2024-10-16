import grpc
from concurrent import futures
import time
import pesoideal_pb2
import pesoideal_pb2_grpc

# Implementação do serviço PesoIdeal
class PesoIdealServiceServicer(pesoideal_pb2_grpc.PesoIdealServiceServicer):

    def CalcularPesoIdeal(self, request, context):
        altura = request.altura
        sexo = request.sexo.upper()

        if sexo == 'M':
            peso_ideal = (72.7 * altura) - 58
        elif sexo == 'F':
            peso_ideal = (62.1 * altura) - 44.7
        else:
            context.set_details("Sexo inválido! Use 'M' ou 'F'.")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return pesoideal_pb2.PesoIdealResponse()

        # Retorna a resposta
        return pesoideal_pb2.PesoIdealResponse(pesoIdeal=peso_ideal)

# Função para iniciar o servidor gRPC
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pesoideal_pb2_grpc.add_PesoIdealServiceServicer_to_server(PesoIdealServiceServicer(), server)

    print("Servidor gRPC iniciado na porta 50051...")
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)  # Mantém o servidor rodando por um dia
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()
