/*
Exercício 9. Crie um método que recebe um array de inteiros positivos e substitui seus elementos de valor ímpar
por -1 e os pares por +1.
 */
package semana11e12;

import java.util.Arrays;

public class Exercicio9 {

    public static void tranformaArray(int[] inteiros) {
        for (int i = 0; i < inteiros.length; i++) {
            if (inteiros[i] % 2 == 0) {
                inteiros[i] = 1;
            } else {
                inteiros[i] = -1;
            }
        }
    }

    public static void transformarArrayOpTernario(int[] inteiros) {
        for (int i = 0; i < inteiros.length; i++) {
            inteiros[i] = inteiros[i] % 2 == 0 ? 1 : -1;
        }
    }

    public static void main(String[] args) {

        int[] arrayTeste = {1, 2, 3, 4, 5, 6, 7};
        tranformaArray(arrayTeste);
        System.out.println(Arrays.toString(arrayTeste));

        int[] arrayTeste2 = {1, 3, 5, 2, 4, 6};
        transformarArrayOpTernario(arrayTeste2);
        System.out.println(Arrays.toString(arrayTeste2));


    }

}
