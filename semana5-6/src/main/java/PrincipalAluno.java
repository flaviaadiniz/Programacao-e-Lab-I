import java.util.Scanner;

public class PrincipalAluno {

    public static void main(String[] args) {

        Aluno aluno1 = new Aluno("Brandamente Brasil", "1585258", 5.0, 9.0);
        Aluno aluno2 = new Aluno("Radigunda Cercená", "2254879", 8.0, 2.0);
        Aluno aluno3 = new Aluno("Vitimado José Araújo", "0085994", 7.0, 1.0);

        //Imprima as informações de cada um dos 3 alunos
        System.out.println(aluno1.imprimeInfo());
        System.out.println();

        System.out.println(aluno2.imprimeInfo());
        System.out.println();

        System.out.println(aluno3.imprimeInfo());
        System.out.println();

        //Altere a nota do Grau A de Radigunda para 9
        aluno2.setGrauA(9.0);

        //Imprima apenas a média final de Radigunda
        System.out.println("Nova média final de Radigunda: " +
                aluno2.calcularMediafinal(aluno2.getGrauA(), aluno2.getGrauB()));
        System.out.println();

        //Imprima somente a matrícula de Vitimado
        System.out.println("Matrícula de Vitimado: " + aluno3.getMatricula());
        System.out.println();

        //Altere a matrícula de Brandamente para 1585228
        aluno1.setMatricula("1585228");
        System.out.println("Nova matrícula de Brandamente: " + aluno1.getMatricula());
        System.out.println();

        //Altere a nota do GB de Radigunda por um valor lido pelo Teclado
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite a nova nota de Grau B para Radigunda: ");
        aluno2.setGrauB(scanner.nextDouble());
        System.out.println("Nova nota de Grau B de Radigunda: " + aluno2.getGrauB());


    }

}
