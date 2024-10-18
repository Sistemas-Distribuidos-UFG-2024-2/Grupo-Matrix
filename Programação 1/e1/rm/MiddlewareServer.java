import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class MiddlewareServer {
    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(12345);
            System.out.println("Middleware servidor em execução na porta 12345...");

            SalarioService service = new SalarioServiceImpl();

            while (true) {
                Socket clientSocket = serverSocket.accept();
                BufferedReader input = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                PrintWriter output = new PrintWriter(clientSocket.getOutputStream(), true);

                // Recebe os dados do cliente (cargo e salário)
                String cargo = input.readLine();
                double salario = Double.parseDouble(input.readLine());

                // Calcula o reajuste usando o serviço
                double salarioReajustado = service.calcularReajuste(cargo, salario);

                // Envia o salário reajustado de volta ao cliente
                output.println(salarioReajustado);

                // Fecha a conexão
                clientSocket.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
