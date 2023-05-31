/*
Exercício 2. Escreva um trecho Java que exiba os valores de um array a double numa mesma linha.
 */

package semana11e12;

public class Exercicio2 {

    public static void main(String[] args) {

        double[] arrayDouble = new double[10];

        for (double value : arrayDouble) {
            System.out.print(value + " ");
        }

    }

}
