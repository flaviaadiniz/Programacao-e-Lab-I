package semana9e10.exercicio1;

public class Programador extends Pessoa {

    private String linguagemFavorita;

    public Programador(String nome, int idade, String linguagemFavorita) {
        super(nome, idade);
        this.linguagemFavorita = linguagemFavorita;
    }

    public String getLinguagemFavorita() {
        return linguagemFavorita;
    }

    public void setLinguagemFavorita(String linguagemFavorita) {
        this.linguagemFavorita = linguagemFavorita;
    }

    @Override
    public void imprimeDados() {
        super.imprimeDados();
        System.out.println("Linguagem Favorita: " + getLinguagemFavorita());
    }


}
