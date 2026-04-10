import grpc
import calculator_pb2
import calculator_pb2_grpc

with grpc.insecure_channel('localhost:50052') as channel:
    stub = calculator_pb2_grpc.CalculadoraStub(channel)
    response = stub.Somar(calculator_pb2.SomaRequest(a=10, b=5))
    print("Resultado:", response.resultado)