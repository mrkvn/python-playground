package main

//go:generate mkdir -p protos
//go:generate protoc --go_out=. --go_opt=paths=source_relative --go-grpc_out=. --go-grpc_opt=paths=source_relative pb/helloworld.proto
