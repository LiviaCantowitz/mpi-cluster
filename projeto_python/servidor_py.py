import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc

class Servico(calculator_pb2_grpc.CalculadoraServicer):
    def Somar(self, request, context):
        return calculator_pb2.SomaResponse(resultado=request.a + request.b)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculadoraServicer_to_server(Servico(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor rodando...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()