import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

// Implementação do objeto remoto
public class PesoIdealImpl extends UnicastRemoteObject implements PesoIdeal {

    // Construtor
    protected PesoIdealImpl() throws RemoteException {
        super();
    }

    // Implementação do método para calcular o peso ideal
    @Override
    public double calcularPesoIdeal(double altura, String sexo) throws RemoteException {
        if (sexo.equalsIgnoreCase("M")) {
            return (72.7 * altura) - 58;
        } else if (sexo.equalsIgnoreCase("F")) {
            return (62.1 * altura) - 44.7;
        } else {
            throw new IllegalArgumentException("Sexo inválido! Use 'M' para masculino ou 'F' para feminino.");
        }
    }
}
