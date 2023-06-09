package main

import (
	"fmt"
	"net/http"
	"tbdhack/server"

	"golang.org/x/net/websocket"
)

func main(){
	server := server.NewServer()
	http.Handle("/", websocket.Handler(server.HandleWS))

	fmt.Println("Listening on port 8080...")
	http.ListenAndServe("127.0.0.1:8080", nil)
}