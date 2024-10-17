import java.rmi.Remote;
import java.rmi.RemoteException;

public interface AposentadoriaService extends Remote {
    String verificarAposentadoria(int idade, int tempoServico) throws RemoteException;
}
