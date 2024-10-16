import java.io.*;
import java.net.*;

public class PesoIdealClient {

    public static void main(String[] args) {
        String serverName = "127.0.0.1"; // Endereço IP do servidor
        int port = 65432; // Porta usada pelo servidor

        try {
            // Conectando ao servidor
            Socket client = new Socket(serverName, port);
            System.out.println("Conectado ao servidor: " + serverName);

            // Preparando os streams de entrada e saída
            OutputStream outToServer = client.getOutputStream();
            PrintWriter out = new PrintWriter(outToServer, true);

            // Pegando os dados de entrada (altura e sexo)
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            System.out.print("Digite a altura: ");
            String altura = br.readLine();
            System.out.print("Digite o sexo (M/F): ");
            String sexo = br.readLine();

            // Enviando dados para o servidor
            String dados = altura + "," + sexo;
            out.println(dados); // Envia os dados como string simples

            // Recebendo a resposta do servidor
            BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
            String resposta = in.readLine();

            System.out.println("Peso ideal calculado: " + resposta);

            // Fechando a conexão
            client.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
