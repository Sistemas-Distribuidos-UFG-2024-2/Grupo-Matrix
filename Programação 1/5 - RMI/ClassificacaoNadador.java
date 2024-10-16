import java.rmi.Remote;
import java.rmi.RemoteException;

// Interface remota
public interface ClassificacaoNadador extends Remote {
    // Método remoto para classificar a idade do nadador
    String classificarNadador(int idade) throws RemoteException;
}
