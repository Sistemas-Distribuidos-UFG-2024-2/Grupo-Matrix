package problemas_programacao1;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class ServidorRMI {
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.createRegistry(1110);
            ICartaService cartaService = new CartaService();
           
            registry.rebind("CartaService", cartaService);

            System.out.println("Servidor RMI pronto.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
