from CoolProp.CoolProp import PropsSI
from concurrent import futures
import grpc

from coolprop_pb2 import (
    PropertyPair,
    FluidProperties,
    CalculationRequest,
    CalculationResponse,
)

import coolprop_pb2_grpc


class CalculationService(coolprop_pb2_grpc.CalculationServiceServicer):
    def Calculate(self, request, context):
        print(request)
        print(context)
        return CalculationResponse(
            result=1.0,
            message="Hello, World!",
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    coolprop_pb2_grpc.add_CalculationServiceServicer_to_server(
        CalculationService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
