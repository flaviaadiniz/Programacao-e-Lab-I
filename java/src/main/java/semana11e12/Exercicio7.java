/*
Exercício 7. Escreva um método que recebe um array de double e devolve a posição onde se encontra o maior valor do
array. Se houver mais de um valor maior, devolver a posição da primeira ocorrência.
 */
package semana11e12;

public class Exercicio7 {

    public static int posicaoMaiorValor(double[] doubleArray) {
        if (doubleArray == null) {
            return -1;
        }

        int posicao = 0;
        for (int i = 1; i < doubleArray.length; i++) {
            if (doubleArray[i] > doubleArray[posicao]) {
                posicao = i;
            }
        }
        return posicao;
    }

    public static void main(String[] args) {

        double[] arrayDouble = {2.6, 2.4, 4.9, 10.9, 5.0, 8.2, 10.9};

        System.out.println(posicaoMaiorValor(arrayDouble));

    }

}
