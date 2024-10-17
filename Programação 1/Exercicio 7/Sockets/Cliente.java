import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Cliente {
    public static void main(String[] args) {
        String host = "localhost";
        int port = 5001;

        try (Socket socket = new Socket(host, port)) {
            // Conexão estabelecida

            // Criar input/output streams
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            
            try (// Leitura de dados do usuário
            Scanner scanner = new Scanner(System.in)) {
                System.out.print("Digite a idade do funcionário: ");
                int idade = scanner.nextInt();
                
                System.out.print("Digite o tempo de serviço do funcionário: ");
                int tempoServico = scanner.nextInt();

                // Enviar dados para o servidor
                out.println(idade + "," + tempoServico);
            }
            // Receber e exibir a resposta do servidor
            String resposta = in.readLine();
            System.out.println("Resposta do servidor: " + resposta);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
