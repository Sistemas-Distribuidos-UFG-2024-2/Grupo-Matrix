import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class ClienteRMI {

    public static void main(String[] args) {
        try {
            // Obtém referência ao registro RMI na máquina local
            Registry registry = LocateRegistry.getRegistry("localhost", 1098);

            // Localiza o serviço remoto pelo nome
            ClassificacaoNadador stub = (ClassificacaoNadador) registry.lookup("ClassificacaoNadador");

            // Lê a idade do usuário
            Scanner scanner = new Scanner(System.in);
            System.out.print("Digite a idade do nadador: ");
            int idade = scanner.nextInt();

            // Chama o método remoto para classificar o nadador
            String categoria = stub.classificarNadador(idade);
            System.out.println("Classificação: " + categoria);

        } catch (Exception e) {
            System.out.println("Erro no cliente RMI: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
