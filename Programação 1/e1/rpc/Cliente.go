package main

import (
	"bufio"
	"bytes"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"strconv"
	"strings"
)

func main() {
	// Ler os dados do usuário
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Digite o nome do funcionário: ")
	nome, _ := reader.ReadString('\n')
	nome = strings.TrimSpace(nome)

	fmt.Print("Digite o cargo do funcionário (operador/programador): ")
	cargo, _ := reader.ReadString('\n')
	cargo = strings.TrimSpace(cargo)

	fmt.Print("Digite o salário do funcionário: ")
	salarioStr, _ := reader.ReadString('\n')
	salarioStr = strings.TrimSpace(salarioStr)
	salario, err := strconv.ParseFloat(salarioStr, 64)
	if err != nil {
		log.Fatalf("Erro ao converter o salário: %v", err)
	}

	// Criar a estrutura de requisição JSON-RPC
	request := map[string]interface{}{
		"jsonrpc": "2.0",
		"method":  "calcular_reajuste",
		"params":  []interface{}{nome, cargo, salario},
		"id":      1,
	}

	// Serializar a estrutura em JSON
	requestBody, err := json.Marshal(request)
	if err != nil {
		log.Fatalf("Erro ao criar o JSON da requisição: %v", err)
	}

	// Fazer a requisição HTTP POST para o servidor JSON-RPC
	resp, err := http.Post("http://localhost:8000", "application/json", bytes.NewBuffer(requestBody))
	if err != nil {
		log.Fatalf("Erro ao fazer a requisição para o servidor: %v", err)
	}
	defer resp.Body.Close()

	// Ler a resposta do servidor
	var result map[string]interface{}
	err = json.NewDecoder(resp.Body).Decode(&result)
	if err != nil {
		log.Fatalf("Erro ao decodificar a resposta do servidor: %v", err)
	}

	// Verificar se houve algum erro na resposta
	if result["error"] != nil {
		log.Fatalf("Erro no cálculo do reajuste: %v", result["error"])
	}

	// Imprimir o resultado do reajuste
	fmt.Println(result["result"])
}
