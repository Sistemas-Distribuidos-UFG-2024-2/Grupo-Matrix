import java.io.*;
import java.net.*;

public class Cliente {
    public static void main(String[] args) {
        String s2Ip = "127.0.0.1";
        int s2Port = 5000;

        try (Socket socket = new Socket()) {
            int attempts = 0;
            boolean connected = false;
            
            while (attempts < 5 && !connected) {
                try {
                    System.out.println("Tentando conectar ao servidor...");
                    socket.connect(new InetSocketAddress(s2Ip, s2Port), 2000);
                    connected = true;
                } catch (IOException e) {
                    System.out.println("Conexão recusada. Tentando novamente...");
                    attempts++;
                    Thread.sleep(2000);
                }
            }

            if (connected) {
                try (OutputStream os = socket.getOutputStream();
                     InputStream is = socket.getInputStream()) {
                    os.write("hello".getBytes());

                    byte[] buffer = new byte[1024];
                    int bytesRead = is.read(buffer);

                    if (bytesRead != -1) {
                        String response = new String(buffer, 0, bytesRead);
                        System.out.println("Resposta recebida: " + response);
                    }
                }
            } else {
                System.out.println("Não foi possível conectar ao servidor após várias tentativas.");
            }
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
