import java.rmi.Remote;
import java.rmi.RemoteException;

public interface SalarioService extends Remote {
    double calcularReajuste(String cargo, double salario) throws RemoteException;
}