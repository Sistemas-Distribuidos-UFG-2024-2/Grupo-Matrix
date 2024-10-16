import java.rmi.Naming;
import java.util.Scanner;

public class ClienteRMI {

    public static void main(String[] args) {
        try {
            // Localiza o serviço remoto no RMI Registry
	    PesoIdeal stub = (PesoIdeal) Naming.lookup("rmi://localhost:1098/PesoIdealService");


            // Recebe os dados do usuário
            Scanner scanner = new Scanner(System.in);
            System.out.print("Digite a altura: ");
            double altura = scanner.nextDouble();
            scanner.nextLine(); // Consome a nova linha
            System.out.print("Digite o sexo (M/F): ");
            String sexo = scanner.nextLine();

            // Chama o método remoto
            double pesoIdeal = stub.calcularPesoIdeal(altura, sexo);
            System.out.println("O peso ideal calculado é: " + pesoIdeal);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
