import java.io.*;
import java.net.*;

public class Cliente {

    public static String[] resolveDomainToIPs(String domain) {
        if (domain.equals("balanceador")) {
            return new String[]{"127.0.0.1", "127.0.0.2"}; // IPs simulados
        }
        return new String[0];
    }

    public static boolean conectaServidor(String ip, int port) {
        try (Socket socket = new Socket()) {
            int tentativas = 0;
            boolean conectado = false;

            while (tentativas < 5 && !conectado) {
                try {
                    System.out.println("Tentando conectar ao IP: " + ip);
                    socket.connect(new InetSocketAddress(ip, port), 2000);
                    conectado = true;
                    System.out.println("Conectado ao servidor no IP: " + ip);

                    try (OutputStream os = socket.getOutputStream();
                         InputStream is = socket.getInputStream()) {
                        os.write("hello".getBytes());

                        byte[] buffer = new byte[1024];
                        int bytesRead = is.read(buffer);

                        if (bytesRead != -1) {
                            String response = new String(buffer, 0, bytesRead);
                            System.out.println("Resposta recebida do IP " + ip + ": " + response);
                        }
                    }
                } catch (IOException e) {
                    System.out.println("Conexão recusada para o IP: " + ip + ". Tentando novamente...");
                    tentativas++;
                    Thread.sleep(2000); // Aguardar antes de tentar novamente
                }
            }

            if (!conectado) {
                System.out.println("Não foi possível conectar ao servidor no IP " + ip + " após várias tentativas.");
            }
            return conectado;
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
            return false;
        }
    }

    public static void main(String[] args) {
        String domain = "balanceador";
        int port = 5000;

        String[] ips = resolveDomainToIPs(domain);

        if (ips.length == 0) {
            System.out.println("Nenhum IP encontrado para o domínio.");
            return;
        }

        final boolean[] conectado = {false};

        Thread threadConexao = new Thread(() -> {
            for (String ip : ips) {
                if (!conectado[0]) {  
                    if (conectaServidor(ip, port)) {
                        conectado[0] = true;  
                        break;
                    }
                }
            }
        });

        Thread threadContadora = new Thread(() -> {
            int aux = 0;
            while (!conectado[0]) {  
                System.out.println("Contando... " + aux++);
                try {
                    Thread.sleep(1000);  
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            System.out.println("Conexão estabelecida, contagem parada.");
        });

        threadConexao.start();
        threadContadora.start();

        try {
            threadConexao.join();
            threadContadora.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
