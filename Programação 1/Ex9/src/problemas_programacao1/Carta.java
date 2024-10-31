package problemas_programacao1;

public class Carta {
    private int valor; 
    private int naipe; 
    
    public Carta(int valor, int naipe) {
        this.valor = valor;
        this.naipe = naipe;
    }

    public String getNome() {
        String[] valores = {"Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei"};
        String[] naipes = {"Ouros", "Paus", "Copas", "Espadas"};

        return valores[this.valor - 1] + " de " + naipes[this.naipe - 1];
    }
}