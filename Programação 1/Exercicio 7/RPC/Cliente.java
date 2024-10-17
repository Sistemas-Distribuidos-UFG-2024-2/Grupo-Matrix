import java.io.*;
import java.net.*;

public class Cliente {
    public static void main(String[] args) {
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

            // Ler idade e tempo de serviço
            System.out.print("Digite sua idade: ");
            int idade = Integer.parseInt(reader.readLine());

            System.out.print("Digite seu tempo de serviço (em anos): ");
            int tempoServico = Integer.parseInt(reader.readLine());

            // Criar a requisição XML
            String requestBody = "<?xml version=\"1.0\"?>\n" +
                    "<methodCall>\n" +
                    "<methodName>pode_aposentar</methodName>\n" +
                    "<params>\n" +
                    "<param><value><int>" + idade + "</int></value></param>\n" +
                    "<param><value><int>" + tempoServico + "</int></value></param>\n" +
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
