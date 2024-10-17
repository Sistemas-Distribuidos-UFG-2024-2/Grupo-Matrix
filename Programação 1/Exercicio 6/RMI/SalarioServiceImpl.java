import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class SalarioServiceImpl extends UnicastRemoteObject implements SalarioService {

    public SalarioServiceImpl() throws RemoteException {
        super();
    }

    @Override
    public Salario calcularSalarioLiquido(String nome, String nivel, double salarioBruto, int dependentes) throws RemoteException {
        double desconto;
        switch (nivel.toUpperCase()) {
            case "A":
                desconto = (dependentes > 0) ? 0.08 : 0.03;
                break;
            case "B":
                desconto = (dependentes > 0) ? 0.10 : 0.05;
                break;
            case "C":
                desconto = (dependentes > 0) ? 0.15 : 0.08;
                break;
            case "D":
                desconto = (dependentes > 0) ? 0.17 : 0.10;
                break;
            default:
                throw new RemoteException("Nível inválido.");
        }
        double salarioLiquido = salarioBruto * (1 - desconto);
        return new Salario(nome, nivel, salarioLiquido);
    }

    public static void main(String[] args) {
        try {
            // Criar e exportar o objeto remoto
            SalarioServiceImpl service = new SalarioServiceImpl();

            // Registrar o serviço no RMI Registry
            Naming.rebind("rmi://localhost:1099/SalarioService", service);

            System.out.println("Servidor RMI está pronto.");
        } catch (Exception e) {
            System.err.println("Erro no servidor: " + e.toString());
        }
    }
}
