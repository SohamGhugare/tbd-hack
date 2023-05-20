package server

import (
	"log"

	socketio "github.com/googollee/go-socket.io"
)

func GetServer() *socketio.Server {
	server := socketio.NewServer(nil)

	server.OnConnect("/", func(s socketio.Conn) error {
		s.SetContext("")
		log.Println("Client connected:", s.ID())
		return nil
	})

	server.OnEvent("/", "chat message", func(s socketio.Conn, msg string) {
		log.Println("Received message:", msg)
		server.BroadcastToRoom("/", "chat", "chat message", msg)
	})

	server.OnDisconnect("/", func(s socketio.Conn, reason string) {
		log.Println("Client disconnected:", s.ID())
	})


	return server
}
