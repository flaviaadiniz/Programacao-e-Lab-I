package semana13e14.biblioteca;

import java.util.Arrays;

public class Biblioteca {

    private Livro[] livros;

    public Livro[] getLivros() {
        return livros;
    }

    public void setLivros(Livro[] livros) {
        this.livros = livros;
    }

    @Override
    public String toString() {
        return "Biblioteca [" +
                "Livros=" + Arrays.toString(livros) +
                ']';
    }



}
