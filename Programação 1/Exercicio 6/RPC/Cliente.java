import java.io.*;
import java.net.*;

public class Cliente {
    public static void main(String[] args) {
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

            // Ler nome do funcionário
            System.out.print("Digite seu nome: ");
            String nome = reader.readLine();

            // Ler nível do funcionário
            System.out.print("Digite seu nível (A, B, C, D): ");
            String nivel = reader.readLine();

            // Ler salário bruto
            System.out.print("Digite seu salário bruto: ");
            double salarioBruto = Double.parseDouble(reader.readLine());

            // Ler número de dependentes
            System.out.print("Digite o número de dependentes: ");
            int dependentes = Integer.parseInt(reader.readLine());

            // Criar a requisição XML
            String requestBody = "<?xml version=\"1.0\"?>\n" +
                    "<methodCall>\n" +
                    "<methodName>calcular_salario_liquido</methodName>\n" +
                    "<params>\n" +
                    "<param><value><string>" + nome + "</string></value></param>\n" +
                    "<param><value><string>" + nivel + "</string></value></param>\n" +
                    "<param><value><double>" + salarioBruto + "</double></value></param>\n" +
                    "<param><value><int>" + dependentes + "</int></value></param>\n" +
                    "</params>\n" +
                    "</methodCall>";

            String request = "POST /RPC2 HTTP/1.0\r\n" +
                    "Content-Type: text/xml\r\n" +
                    "Content-Length: " + requestBody.length() + "\r\n" +
                    "\r\n" +
                    requestBody;

            // Conectar ao servidor
            Socket socket = new Socket("localhost", 8000);
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            // Enviar requisição
            System.out.println("Requisição enviada: " + request);
            out.print(request);
            out.flush();

            // Ler resposta
            String responseLine;
            while ((responseLine = in.readLine()) != null) {
                System.out.println("Resposta do servidor: " + responseLine);
            }

            // Fechar conexão
            in.close();
            out.close();
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
