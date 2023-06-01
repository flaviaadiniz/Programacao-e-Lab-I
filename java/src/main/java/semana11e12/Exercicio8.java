/*
Exercício 8. Faça um método que devolve um array de números inteiros lidos do teclado. O tamanho do array
também deve ser solicitado pelo teclado ao usuário.
 */
package semana11e12;

import java.util.Arrays;
import java.util.Scanner;

public class Exercicio8 {

    public static int[] criarArray() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Vamos criar um array de números inteiros!");
        System.out.print("Digite a quantidade de números que deseja salvar no array: ");
        int[] arrayInt = new int[scanner.nextInt()];

        System.out.println("Agora vamos salvar os números!");
        for (int i = 0; i < arrayInt.length; i++) {
            System.out.print("Digite um número: ");
            arrayInt[i] = scanner.nextInt();
        }

        scanner.close();

        return arrayInt;
    }

    public static void main(String[] args) {

        System.out.println(Arrays.toString(criarArray()));

    }

}
