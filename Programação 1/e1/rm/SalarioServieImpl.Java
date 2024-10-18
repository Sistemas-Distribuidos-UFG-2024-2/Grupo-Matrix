import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class SalarioServiceImpl extends UnicastRemoteObject implements SalarioService {
    protected SalarioServiceImpl() throws RemoteException {
        super();
    }

    @Override
    public double calcularReajuste(String cargo, double salario) throws RemoteException {
        double reajuste = 0;
        if ("operador".equalsIgnoreCase(cargo)) {
            reajuste = salario * 1.20;  // Aumento de 20%
        } else if ("programador".equalsIgnoreCase(cargo)) {
            reajuste = salario * 1.18;  // Aumento de 18%
        } else {
            reajuste = salario;  // Sem reajuste para outros cargos
        }
        return reajuste;
    }
}
