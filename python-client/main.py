import asyncio
import logging

import grpc
import todo_pb2
import todo_pb2_grpc


async def run() -> None:
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = todo_pb2_grpc.TodoServiceStub(channel)
        response: todo_pb2.Todo = await stub.CreateTodo(
            todo_pb2.NewTodo(
                name="new python todo",
                description="todo made from python client",
                done=False
            )
        )

    print(response)
    print(type(response))
    print(response.id)
    print(response.name)
    print(response.description)
    print(response.done)


if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(run())
