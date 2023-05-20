package semana5e6.livraria;

import java.util.Scanner;

public class Principal {

    public static void main(String[] args) {

        String titulo;
        String autor;
        String ano;
        double preco;
        int paginas;

        Scanner scanner = new Scanner(System.in);

        System.out.println("Vamos cadastrar 3 livros!");

        System.out.println("- LIVRO 1 -");
        System.out.print("Título: ");
        titulo = scanner.nextLine();
        System.out.print("Autor: ");
        autor = scanner.nextLine();
        System.out.print("Ano publicado: ");
        ano = scanner.nextLine();
        System.out.print("Preço: ");
        preco = scanner.nextDouble();
        System.out.print("Páginas: ");
        paginas = scanner.nextInt();
        scanner.nextLine();
        Livro livro1 = new Livro(titulo, autor, ano, preco, paginas);


        System.out.println("- LIVRO 2 -");
        System.out.print("Título: ");
        titulo = scanner.nextLine();
        System.out.print("Autor: ");
        autor = scanner.nextLine();
        System.out.print("Ano publicado: ");
        ano = scanner.nextLine();
        System.out.print("Preço: ");
        preco = scanner.nextDouble();
        System.out.print("Páginas: ");
        paginas = scanner.nextInt();
        scanner.nextLine();
        Livro livro2 = new Livro(titulo, autor, ano, preco, paginas);


        System.out.println("- LIVRO 3 -");
        System.out.print("Título: ");
        titulo = scanner.nextLine();
        System.out.print("Autor: ");
        autor = scanner.nextLine();
        System.out.print("Ano publicado: ");
        ano = scanner.nextLine();
        System.out.print("Preço: ");
        preco = scanner.nextDouble();
        System.out.print("Páginas: ");
        paginas = scanner.nextInt();
        scanner.nextLine();
        Livro livro3 = new Livro(titulo, autor, ano, preco, paginas);


        System.out.println("Preço por página do livro 1: " +
                livro1.calcularPrecoPorPagina(livro1.getPreco(), livro1.getPaginas()));

        System.out.println("Preço por página do livro 2: " +
                livro1.calcularPrecoPorPagina(livro2.getPreco(), livro2.getPaginas()));

        System.out.println("Preço por página do livro 3: " +
                livro1.calcularPrecoPorPagina(livro3.getPreco(), livro3.getPaginas()));


        livro1.imprimeInformacoes();
        livro2.imprimeInformacoes();
        livro3.imprimeInformacoes();


        scanner.close();


        }

    }
