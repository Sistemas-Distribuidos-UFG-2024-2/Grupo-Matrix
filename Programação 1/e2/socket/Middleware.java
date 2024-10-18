import java.io.*;
import java.net.*;

public class Middleware {

    public static void main(String[] args) {
        try {
            ServerSocket middlewareSocket = new ServerSocket(5000);  // Porta do middleware
            System.out.println("Middleware aguardando conexões...");

            while (true) {
                Socket clientSocket = middlewareSocket.accept();
                System.out.println("Cliente conectado ao middleware.");

                BufferedReader inClient = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                PrintWriter outClient = new PrintWriter(clientSocket.getOutputStream(), true);

                String metodo = inClient.readLine();
                String nome = inClient.readLine();
                String sexo = inClient.readLine();
                String idadeStr = inClient.readLine();

                Socket serverSocket = new Socket("localhost", 6000);  // Porta do servidor
                PrintWriter outServer = new PrintWriter(serverSocket.getOutputStream(), true);
                BufferedReader inServer = new BufferedReader(new InputStreamReader(serverSocket.getInputStream()));

                outServer.println(metodo);
                outServer.println(nome);
                outServer.println(sexo);
                outServer.println(idadeStr);

                String resposta = inServer.readLine();
                System.out.println("Resposta do servidor: " + resposta);

                outClient.println(resposta);

                serverSocket.close();
                clientSocket.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
