import java.rmi.Remote;
import java.rmi.RemoteException;

// Interface remota
public interface PesoIdeal extends Remote {
    // Método para calcular o peso ideal
    public double calcularPesoIdeal(double altura, String sexo) throws RemoteException;
}
