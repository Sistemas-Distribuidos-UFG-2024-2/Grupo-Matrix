import java.io.*;
import java.net.*;

public class Servidor {

    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(6000); 
            System.out.println("Servidor aguardando conexões...");

            while (true) {
                Socket socket = serverSocket.accept();
                System.out.println("Cliente conectado.");

                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

                String metodo = in.readLine(); 
                String nome = in.readLine();
                String sexo = in.readLine();
                int idade = Integer.parseInt(in.readLine());

                String resultado = verificarMaioridade(nome, sexo, idade);
                out.println(resultado);

                socket.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static String verificarMaioridade(String nome, String sexo, int idade) {
        if (sexo.equalsIgnoreCase("masculino") && idade >= 18) {
            return nome + " já atingiu a maioridade.";
        } else if (sexo.equalsIgnoreCase("feminino") && idade >= 21) {
            return nome + " já atingiu a maioridade.";
        } else {
            return nome + " não atingiu a maioridade.";
        }
    }
}
