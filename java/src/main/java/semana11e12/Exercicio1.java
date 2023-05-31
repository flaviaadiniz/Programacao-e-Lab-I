/* Exercício 1. Para cada conjunto de valores abaixo, escreva o código Java, usando laço(s), que preencha um
array com os valores: */
package semana11e12;

import java.util.Arrays;

public class Exercicio1 {

    public static void main(String[] args) {

        // a. 10  9  8  7  6  5  4  3  2  1
        int[] arrayA = new int[10];
        int contA = 10;
        for (int i = 0; i < arrayA.length; i++) {
            arrayA[i] = contA--;
        }
        System.out.println(Arrays.toString(arrayA));


        // b. 0  1  4  9  16  25  36  49  64  81  100
        int[] arrayB = new int[11];
        for (int i = 0; i < arrayB.length; i++) {
            arrayB[i] = i*i;
        }
        System.out.println(Arrays.toString(arrayB));


        // c. 1  2  3  4  5  10  20  30  40  50
        int[] arrayC = new int[10];
        int cont = 10;
        for (int i = 0; i < arrayC.length; i++) {
            if (i < 5) {
                arrayC[i] = i + 1;
            } else {
                arrayC[i] = cont;
                cont += 10;
            }
        }
        System.out.println(Arrays.toString(arrayC));


        // d. 3  4  7  12  19  28  39  52  67  84
        int[] arrayD = new int[10];
        for (int i = 0; i < arrayD.length; i++) {
            arrayD[i] = (i*i) + 3;
        }
        System.out.println(Arrays.toString(arrayD));

    }

}
