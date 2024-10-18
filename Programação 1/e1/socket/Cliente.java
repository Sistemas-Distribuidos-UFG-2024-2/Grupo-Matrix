import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Cliente {
    public static void main(String[] args) {
        String servidorHost = "localhost";
        int porta = 12345;

        try {
            Socket socket = new Socket(servidorHost, porta);

            PrintWriter saida = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader entrada = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            Scanner scanner = new Scanner(System.in);

            System.out.print("Digite o nome do funcionário: ");
            String nome = scanner.nextLine();

            System.out.print("Digite o cargo do funcionário (operador/programador): ");
            String cargo = scanner.nextLine();

            System.out.print("Digite o salário do funcionário: ");
            double salario = scanner.nextDouble();

            saida.println(nome + "," + cargo + "," + salario);

            String resposta = entrada.readLine();
            System.out.println("Resposta do servidor: " + resposta);

            saida.close();
            entrada.close();
            socket.close();
            scanner.close();
        } catch (IOException e) {
            System.err.println("Erro na comunicação: " + e.getMessage());
        }
    }
}
