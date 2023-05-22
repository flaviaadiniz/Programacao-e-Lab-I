package semana9e10.exercicio1;

public class Melancia extends Fruta {

    private double precoAdicional;
    private boolean epoca;

    public Melancia(String nome, double preco, double precoAdicional, boolean epoca) {
        super(nome, preco);
        this.precoAdicional = precoAdicional;
        this.epoca = epoca;
    }

    public double calculaPrecoFinal() {
        return epoca ? getPreco() : getPreco() + precoAdicional;
    }

    public double getPrecoAdicional() {
        return precoAdicional;
    }

    public void setPrecoAdicional(double precoAdicional) {
        this.precoAdicional = precoAdicional;
    }

    public boolean getEpoca() {
        return epoca;
    }

    public void setEpoca(boolean epoca) {
        this.epoca = epoca;
    }

}
