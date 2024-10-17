import java.io.*;
import java.net.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class AdaptadorPy {
    @SuppressWarnings("resource")
    public static void main(String[] args) {
        try {
            // Inicia o servidor socket para escutar as requisições do cliente Python
            ServerSocket serverSocket = new ServerSocket(5000);
            System.out.println("Adaptador Socket Java está pronto e escutando na porta 5000...");

            // Conectar ao servidor RMI
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            SalarioService salarioService = (SalarioService) registry.lookup("SalarioService");

            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Cliente conectado...");

                // Ler dados do cliente Python
                BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                String input = in.readLine();
                String[] partes = input.split(",");
                
                String nome = partes[0];
                String nivel = partes[1];
                double salarioBruto = Double.parseDouble(partes[2]);
                int dependentes = Integer.parseInt(partes[3]);

                // Chamar o serviço RMI
                Salario salario = salarioService.calcularSalarioLiquido(nome, nivel, salarioBruto, dependentes);

                // Enviar o resultado de volta ao cliente Python
                PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
                out.println("Salário Líquido de " + salario.getNome() + " (Nível " + salario.getNivel() + "): " + salario.getSalarioLiquido());

                // Fechar conexão
                clientSocket.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
