import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Servidor {
    public static void main(String[] args) {
        try {
            AposentadoriaService service = new AposentadoriaServiceImpl();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("AposentadoriaService", service);
            System.out.println("Servidor de Aposentadoria está pronto...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
