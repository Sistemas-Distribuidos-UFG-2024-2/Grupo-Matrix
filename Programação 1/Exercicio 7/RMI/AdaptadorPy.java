import java.io.*;
import java.net.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class AdaptadorPy {
    public static void main(String[] args) {
        try {
            // Inicia o servidor socket para escutar as requisições do cliente Python
            @SuppressWarnings("resource")
            ServerSocket serverSocket = new ServerSocket(5000);
            System.out.println("Adaptador Socket Java está pronto e escutando na porta 5000...");

            // Conectar ao servidor RMI
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            AposentadoriaService aposentadoriaService = (AposentadoriaService) registry.lookup("AposentadoriaService");

            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Cliente conectado...");

                // Ler dados do cliente Python
                BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                String input = in.readLine();
                String[] partes = input.split(",");

                int idade = Integer.parseInt(partes[0]);
                int tempoServico = Integer.parseInt(partes[1]);

                // Chamar o serviço RMI
                String resultado = aposentadoriaService.verificarAposentadoria(idade, tempoServico);

                // Enviar o resultado de volta ao cliente Python
                PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
                out.println(resultado);

                // Fechar conexão
                clientSocket.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
