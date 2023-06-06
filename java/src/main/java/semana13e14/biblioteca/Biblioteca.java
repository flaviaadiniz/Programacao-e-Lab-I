package semana13e14.biblioteca;

import java.util.Arrays;

public class Biblioteca {

    private Livro[] livros;

    public Biblioteca(int quantLivros) {
        this.livros = new Livro[quantLivros];
    }

    public boolean insereLivro(Livro livro) {
        boolean livroInserido = false;
        for (int i = 0; i < livros.length; i++) {
            if (livros[i] == null) {
                livros[i] = livro;
                livroInserido = true;
                break;
            } else {
                livroInserido = false;
            }
        }
        return livroInserido;
    }

    public Livro procuraLivroPorTitulo(String titulo) {
        Livro livro = new Livro();
        for (Livro l : livros) {
            if (l.getTitulo() == titulo) {
                livro = l;
                break;
            } else {
                livro = null;
            }
        }
        return livro;
    }

    public double verificaDesconto(String titulo) {
        double desconto = 0;
        for (Livro l : livros) {
            if (l instanceof Novo) {
                desconto = ((Novo) l).getDesconto();
                break;
            } else {
                desconto = -1;
            }
        }
        return desconto;
    }

    public void imprimeEdicoes() {
        for (int i = 0; i < livros.length; i++) {
            if (livros[i] instanceof Antigo) {
                System.out.println("Título: " + livros[i].getTitulo() +
                        "| Edição: " + ((Antigo) livros[i]).getNumeroEdicao());
            }
        }
    }

    public void imprimeLivroPorAno() {
        
    }

    public double calculaMediaPrecos() {
        double somaValores = 0;
        for (int i = 0; i < livros.length; i++) {
            somaValores += livros[i].getPreco();
        }
        return somaValores / livros.length;
    }

    public Livro livroComMaiorTitulo() {
        int maiorTitulo = 0;
        Livro livroComMaiorTitulo = new Livro();

        for (Livro livro : livros) {
            if (livro.getTitulo().length() > maiorTitulo) {
                maiorTitulo = livro.getTitulo().length();
                livroComMaiorTitulo = livro;
            }
        }

        return livroComMaiorTitulo;
    }


    public Livro[] getLivros() {
        return livros;
    }

    public void setLivros(Livro[] livros) {
        this.livros = livros;
    }

    @Override
    public String toString() {
        return "Biblioteca [" +
                "Livros: " + Arrays.toString(livros) +
                ']';
    }

}
