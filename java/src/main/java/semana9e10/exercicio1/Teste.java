package semana9e10.exercicio1;

import java.util.Scanner;

public class Teste {

    public static void main(String[] args) {

        Banana banana = new Banana("Banana", 3.9, "banana");
        Melancia melancia = new Melancia("Melancia", 2.7, 1.8, true);
        Programador programador = new Programador("Flávia", 39, "Java");
        Aluno aluno = new Aluno("Diego", 19, 10.0);

        //testando métodos de acesso
        System.out.println(banana.getNome());
        System.out.println(melancia.getPreco());
        System.out.println(programador.getLinguagemFavorita());
        System.out.println(aluno.getIdade());

        //instanciando pessoa
        Pessoa p;

        Scanner scanner = new Scanner(System.in);

        System.out.println("Vamos cadastrar uma pessoa." +
                "\nPara cadastrar um PROGRAMADOR digite 1. \nPara cadastrar um aluno digite 2.");
        int opcao = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Nome: ");
        String nome = scanner.nextLine();

        System.out.print("Idade: ");
        int idade = scanner.nextInt();
        scanner.nextLine();

        if (opcao == 1) {

            System.out.print("Linguagem favorita: ");
            String linguagem = scanner.nextLine();

            p = new Programador(nome, idade, linguagem);
            System.out.println("Linguagem favorita: " + linguagem);

        } else {

            System.out.print("Nota: ");
            int nota = scanner.nextInt();

            p = new Aluno(nome, idade, nota);
            System.out.println("Nota do aluno: " + nota);
        }

        scanner.close();
    }

}
