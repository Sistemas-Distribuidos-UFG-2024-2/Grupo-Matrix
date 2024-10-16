import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class ServidorRMI {

    public static void main(String[] args) {
        try {
            // Cria uma instância do serviço
            PesoIdealImpl pesoIdeal = new PesoIdealImpl();
            
            // Inicia o registro RMI em uma porta diferente, como 1098
            LocateRegistry.createRegistry(1098);
            
            // Registra o serviço no RMI Registry
            Naming.rebind("rmi://localhost:1098/PesoIdealService", pesoIdeal);

            System.out.println("Servidor RMI pronto e aguardando chamadas de clientes...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
