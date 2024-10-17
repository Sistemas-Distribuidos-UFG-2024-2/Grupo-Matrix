import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;

public class AposentadoriaServiceImpl extends UnicastRemoteObject implements AposentadoriaService {

    protected AposentadoriaServiceImpl() throws RemoteException {
        super();
    }

    @Override
    public String verificarAposentadoria(int idade, int tempoServico) throws RemoteException {
        if (idade >= 65 || tempoServico >= 30 || (idade >= 60 && tempoServico >= 25)) {
            return "O funcionário pode se aposentar.";
        } else {
            return "O funcionário NÃO pode se aposentar.";
        }
    }
}
