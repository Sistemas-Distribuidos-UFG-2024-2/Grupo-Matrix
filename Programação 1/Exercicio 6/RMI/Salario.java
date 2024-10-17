import java.io.Serializable;

public class Salario implements Serializable {
    private String nome;
    private String nivel;
    private double salarioLiquido;

    public Salario(String nome, String nivel, double salarioLiquido) {
        this.nome = nome;
        this.nivel = nivel;
        this.salarioLiquido = salarioLiquido;
    }

    public String getNome() {
        return nome;
    }

    public String getNivel() {
        return nivel;
    }

    public double getSalarioLiquido() {
        return salarioLiquido;
    }
}
