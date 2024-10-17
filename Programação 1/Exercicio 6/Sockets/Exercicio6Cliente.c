#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <winsock2.h> // Usar winsock2.h em vez de arpa/inet.h
#include <ws2tcpip.h> // Para funções de rede avançadas

#define PORT 65432
#define BUFFER_SIZE 1024

int main() {
    WSADATA wsaData; // Estrutura para informações sobre o Winsock
    int sock;
    struct sockaddr_in server_address;
    char buffer[BUFFER_SIZE];
    char nome[50], nivel[2];
    double salario_bruto;
    int num_dependentes;

    // Inicializar o Winsock
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        perror("Erro ao inicializar o Winsock");
        return -1;
    }

    // Criar o socket
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) == INVALID_SOCKET) {
        perror("Erro ao criar socket");
        WSACleanup(); // Limpar o Winsock
        return -1;
    }

    // Configurar o endereço do servidor
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(PORT);
    server_address.sin_addr.s_addr = inet_addr("127.0.0.1"); // Usar inet_addr para definir o IP

    // Conectar ao servidor
    if (connect(sock, (struct sockaddr*)&server_address, sizeof(server_address)) == SOCKET_ERROR) {
        perror("Erro ao conectar ao servidor");
        closesocket(sock); // Fechar o socket
        WSACleanup(); // Limpar o Winsock
        return -1;
    }

    // Coletar os dados do funcionário via terminal
    printf("Digite o nome do funcionario: ");
    fgets(nome, sizeof(nome), stdin);
    nome[strcspn(nome, "\n")] = '\0';  // Remover o newline da entrada

    printf("Digite o nivel do funcionario (A, B, C ou D): ");
    fgets(nivel, sizeof(nivel), stdin);
    nivel[strcspn(nivel, "\n")] = '\0';  // Remover o newline

    printf("Digite o salario bruto do funcionario: ");
    scanf("%lf", &salario_bruto);

    printf("Digite o numero de dependentes do funcionario: ");
    scanf("%d", &num_dependentes);

    // Enviar os dados para o servidor
    snprintf(buffer, sizeof(buffer), "%s,%s,%.2f,%d", nome, nivel, salario_bruto, num_dependentes);
    send(sock, buffer, strlen(buffer), 0);

    // Receber a resposta do servidor
    int bytes_recebidos = recv(sock, buffer, BUFFER_SIZE - 1, 0); // Usar recv em vez de read
    if (bytes_recebidos < 0) {
        perror("Erro ao receber dados");
        closesocket(sock); // Fechar o socket
        WSACleanup(); // Limpar o Winsock
        return -1;
    }
    buffer[bytes_recebidos] = '\0';  // Adicionar o terminador nulo

    // Exibir a resposta
    printf("Resposta do servidor: %s\n", buffer);

    // Fechar o socket
    closesocket(sock); // Fechar o socket
    WSACleanup(); // Limpar o Winsock

    return 0;
}
