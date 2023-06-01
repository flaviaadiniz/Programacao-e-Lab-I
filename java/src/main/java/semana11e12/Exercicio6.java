/*
Exercício 6. Escreva um método que recebe um array de inteiros a e devolve um array de boolean onde, cada posição
indique true se o elemento da posição correspondente de a é positivo e false caso seja negativo ou zero.
 */
package semana11e12;

import java.util.Arrays;

public class Exercicio6 {

    public static boolean[] inteirosParaBoolean(int[] arrayInteiros) {
        if (arrayInteiros == null) {
            return null;
        }

        boolean[] arrayBoolean = new boolean[arrayInteiros.length];
        for (int i = 0; i < arrayInteiros.length; i++) {
            arrayBoolean[i] = arrayInteiros[i] > 0;
        }
        return arrayBoolean;
    }

    public static void main(String[] args) {

        int[] inteiros = {-2, 10, 56, 0, -24, 100, -2345, 0, 10};

        System.out.println(Arrays.toString(inteirosParaBoolean(inteiros)));

    }

}
