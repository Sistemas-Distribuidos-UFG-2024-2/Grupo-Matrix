package problemas_programacao1;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class CartaService extends UnicastRemoteObject implements ICartaService {
    public CartaService() throws RemoteException {
        super();
    }

    @Override
    public String getNomeDaCarta(int valor, int naipe) throws RemoteException {
        Carta carta = new Carta(valor, naipe);
        return carta.getNome();
    }
}