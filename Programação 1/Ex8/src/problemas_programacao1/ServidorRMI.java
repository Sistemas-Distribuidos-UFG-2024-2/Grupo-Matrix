package problemas_programacao1;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class ServidorRMI {

	public static void main(String[] args) {
		try {
            // Cria um registro RMI local na porta 1099 (padrão)
			Registry registry = LocateRegistry.createRegistry(1103);			
			// Cria e exporta um objeto remoto
			ICalculaCredito calculacredito = new CalculaCredito();

            // Vincula o objeto remoto ao nome "Calculadora"
            registry.rebind("CalculaCredito", calculacredito);

            System.out.println("Servidor RMI pronto.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
