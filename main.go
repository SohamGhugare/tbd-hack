package main

import (
	"log"
	"net/http"
	"tbdhack/server"
)

func main(){
	server := server.GetServer()

	go server.Serve()
	defer server.Close()

	http.Handle("/socket.io/", server)
	log.Println("Server started on localhost:8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}