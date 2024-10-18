package main

import (
	"fmt"
	"log"
	"net/rpc"
)

type Args struct {
	Nome  string
	Sexo  string
	Idade int
}

func main() {
	client, err := rpc.DialHTTP("tcp", "localhost:1234")
	if err != nil {
		log.Fatal("Erro ao conectar ao servidor:", err)
	}

	var nome, sexo string
	var idade int

	fmt.Print("Digite o nome: ")
	fmt.Scanln(&nome)
	fmt.Print("Digite o sexo (masculino/feminino): ")
	fmt.Scanln(&sexo)
	fmt.Print("Digite a idade: ")
	fmt.Scanln(&idade)

	var resultado string
	err = client.Call("VerificarMaioridade", []interface{}{nome, sexo, idade}, &resultado)
	if err != nil {
		log.Fatal("Erro ao chamar método RPC:", err)
	}

	fmt.Println("Resposta do servidor:", resultado)
}
