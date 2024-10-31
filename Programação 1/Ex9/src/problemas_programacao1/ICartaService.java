package problemas_programacao1;
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface ICartaService extends Remote {
    String getNomeDaCarta(int valor, int naipe) throws RemoteException;
}