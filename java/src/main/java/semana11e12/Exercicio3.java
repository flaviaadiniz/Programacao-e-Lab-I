/*
Exercício 3. Escreva um trecho Java que leia 10 valores double do teclado e armazene-os num array d.
 */

package semana11e12;

import java.util.Arrays;
import java.util.Scanner;

public class Exercicio3 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        double[] d = new double[10];

        for (int i = 0; i < d.length; i++) {
            System.out.print("Digite um número: ");
            d[i] = scanner.nextDouble();
        }

        System.out.println(Arrays.toString(d));

        scanner.close();


    }

}
