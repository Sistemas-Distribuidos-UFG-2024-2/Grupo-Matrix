import java.io.*;
import java.net.*;

public class Cliente {
    public static void main(String[] args) {
        String servidorHost = "localhost";  // IP do servidor
        int portaServidor = 12345;          // Porta do servidor

        try {
            // Conecta ao servidor
            Socket socket = new Socket(servidorHost, portaServidor);
            System.out.println("Conectado ao servidor: " + servidorHost);

            // Cria streams para comunicação com o servidor
            BufferedReader entradaServidor = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter saidaServidor = new PrintWriter(socket.getOutputStream(), true);

            // Lê a idade do nadador do usuário
            BufferedReader leitorConsole = new BufferedReader(new InputStreamReader(System.in));
            System.out.print("Digite a idade do nadador: ");
            String idade = leitorConsole.readLine();

            // Envia a idade ao servidor
            saidaServidor.println(idade);

            // Recebe a categoria do nadador do servidor
            String resposta = entradaServidor.readLine();
            System.out.println("Classificação: " + resposta);

            // Fecha a conexão
            socket.close();

        } catch (IOException e) {
            System.out.println("Erro na comunicação com o servidor: " + e.getMessage());
        }
    }
}
