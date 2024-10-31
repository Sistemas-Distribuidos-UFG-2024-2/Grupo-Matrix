package problemas_programacao1;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class ClienteRMI {
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("localhost", 1110);
            ICartaService cartaService = (ICartaService) registry.lookup("CartaService");

            int valor = 1; 
            int naipe = 2; 
   
            String nomeDaCarta = cartaService.getNomeDaCarta(valor, naipe);
            System.out.println("Nome da carta: " + nomeDaCarta);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
