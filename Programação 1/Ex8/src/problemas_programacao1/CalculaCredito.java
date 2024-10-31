package problemas_programacao1;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class CalculaCredito extends UnicastRemoteObject implements ICalculaCredito {

	public CalculaCredito() throws RemoteException {
		super();
	}
	
	public int percentual(double saldo_medio) throws RemoteException{
		if (saldo_medio >=0 && saldo_medio <=200) {
			return 0;
		}
		else if(saldo_medio >=201 && saldo_medio <=400) {
			return 20;
		}
		else if(saldo_medio >=401 && saldo_medio <=600) {
			return 30;
		}
		return 40;	
	}
}
