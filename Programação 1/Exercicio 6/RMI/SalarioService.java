import java.rmi.Remote;
import java.rmi.RemoteException;

public interface SalarioService extends Remote {
    Salario calcularSalarioLiquido(String nome, String nivel, double salarioBruto, int dependentes) throws RemoteException;
}