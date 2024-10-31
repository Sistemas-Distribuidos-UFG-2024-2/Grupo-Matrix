package problemas_programacao1;
import java.rmi.Remote;
import java.rmi.RemoteException;


public interface ICalculaCredito extends Remote{
	int percentual(double saldo_medio) throws RemoteException;;
}
