package livraria;

public class Livro {

    private String titulo;
    private String autor;
    private String anoPublicacao;
    private double preco;
    private int paginas;


    public Livro(String titulo, String autor, String anoPublicacao, double preco, int paginas) {
        this.titulo = titulo;
        this.autor = autor;
        this.anoPublicacao = anoPublicacao;
        this.preco = preco;
        this.paginas = paginas;
    }

    public double calcularPrecoPorPagina(double preco, int paginas) {
        return preco / paginas;
    }

    public void imprimeInformacoes() {
        System.out.println("Título: " + getTitulo() +
                "\nAutor: " + getAutor() +
                "\nAno: " + getAnoPublicacao() +
                "\nPreço: R$" + getPreco() +
                "\nPáginas: " + getPaginas() +
                "\nPreço por página: R$" + calcularPrecoPorPagina(getPreco(), getPaginas()));
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public String getAnoPublicacao() {
        return anoPublicacao;
    }

    public void setAnoPublicacao(String anoPublicacao) {
        this.anoPublicacao = anoPublicacao;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public int getPaginas() {
        return paginas;
    }

    public void setPaginas(int paginas) {
        this.paginas = paginas;
    }


}
