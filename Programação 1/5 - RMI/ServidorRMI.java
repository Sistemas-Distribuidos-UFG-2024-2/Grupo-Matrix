import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class ServidorRMI extends UnicastRemoteObject implements ClassificacaoNadador {

    // Construtor da classe, necessário para UnicastRemoteObject
    protected ServidorRMI() throws RemoteException {
        super();
    }

    // Implementação do método remoto para classificar o nadador
    @Override
    public String classificarNadador(int idade) throws RemoteException {
        if (idade >= 5 && idade <= 7) {
            return "infantil A";
        } else if (idade >= 8 && idade <= 10) {
            return "infantil B";
        } else if (idade >= 11 && idade <= 13) {
            return "juvenil A";
        } else if (idade >= 14 && idade <= 17) {
            return "juvenil B";
        } else if (idade >= 18) {
            return "adulto";
        } else {
            return "Idade fora das categorias.";
        }
    }

    // Função principal para iniciar o servidor
    public static void main(String[] args) {
        try {
            // Cria uma instância do servidor
            ServidorRMI servidor = new ServidorRMI();

            // Registra o serviço RMI na porta padrão 1099
            Registry registry = LocateRegistry.createRegistry(1098);
            registry.rebind("ClassificacaoNadador", servidor);

            System.out.println("Servidor RMI está pronto.");
        } catch (RemoteException e) {
            System.out.println("Erro no servidor RMI: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
