import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class ClienteSalario {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // Localizar o registro RMI
            Registry registry = LocateRegistry.getRegistry("localhost", 1099); // Endereço do servidor
            SalarioService salarioService = (SalarioService) registry.lookup("SalarioService");

            // Coletar dados do usuário
            System.out.print("Digite o nome do funcionário: ");
            String nome = scanner.nextLine();

            System.out.print("Digite o nível do funcionário (A, B, C ou D): ");
            String nivel = scanner.nextLine();

            System.out.print("Digite o salário bruto do funcionário: ");
            double salarioBruto = scanner.nextDouble();

            System.out.print("Digite o número de dependentes do funcionário: ");
            int dependentes = scanner.nextInt();

            // Chamar o método remoto
            Salario salario = salarioService.calcularSalarioLiquido(nome, nivel, salarioBruto, dependentes);

            // Exibir o resultado
            System.out.printf("Nome: %s, Nível: %s, Salário Líquido: %.2f%n", 
                              salario.getNome(), salario.getNivel(), salario.getSalarioLiquido());

        } catch (Exception e) {
            System.err.println("Erro no cliente: " + e.toString());
        } finally {
            scanner.close();
        }
    }
}
