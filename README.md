### Commands

```bash
# Generate golang proto

protoc --go_out=. --go_opt=paths=source_relative --go-grpc_out=. --go-grpc_opt=paths=source_relative proto/todo.proto

# Start golang server and client
# start server
go run server/main.go

# start client
go run client/main.go

# Generate python proto
cd python-client
# create environment
python3 -m venv env
pip install -r requirements.txt
python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. .todo.proto

# Start python client
python main.py
```

NOTE: used insecure_server