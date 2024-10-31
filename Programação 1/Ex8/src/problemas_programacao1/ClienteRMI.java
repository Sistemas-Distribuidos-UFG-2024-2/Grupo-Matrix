package problemas_programacao1;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class ClienteRMI {
    public static void main(String[] args) {
        try {
            // Localiza o registro RMI na máquina e porta padrão
            Registry registry = LocateRegistry.getRegistry("localhost", 1103);

            // Obtém o stub para o objeto remoto pelo nome
            ICalculaCredito calculacredito = (ICalculaCredito) registry.lookup("CalculaCredito");

            // Chama o método remoto
            double resultado = calculacredito.percentual(500);
            
            if(resultado == 0) {
            	System.out.println("nenhum crédito");
            }else {
            	System.out.println(resultado + "% do valor do saldo médio ");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}