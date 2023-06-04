package semana13e14.biblioteca;

public class Antigo extends Livro {

    private int numeroEdicao;

    public Antigo() {

    }

    public Antigo(String titulo, String autor, double preco, int anoCriacao, int numeroEdicao) {
        super(titulo, autor, preco, anoCriacao);
        this.numeroEdicao = numeroEdicao;
    }

    public int getNumeroEdicao() {
        return numeroEdicao;
    }

    public void setNumeroEdicao(int numeroEdicao) {
        this.numeroEdicao = numeroEdicao;
    }

    @Override
    public String toString() {
        return super.toString() +
                "Número de edição: " + numeroEdicao +
                "]";
    }
}
