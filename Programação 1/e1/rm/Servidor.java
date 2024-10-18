import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class Servidor {
    public static void main(String[] args) {
        try {
            LocateRegistry.createRegistry(1099);  // Porta padrão do RMI
            SalarioService service = new SalarioServiceImpl();
            Naming.rebind("rmi://localhost/SalarioService", service);
            System.out.println("Servidor RMI pronto.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
