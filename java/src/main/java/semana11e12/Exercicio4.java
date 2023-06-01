/*
Exercício 4. Crie um método que recebe um array de inteiros e retorna a quantidade de elementos do array que são
números negativos.
 */

package semana11e12;

public class Exercicio4 {

    public static int quantNegativos(int[] vetor) {
        int cont = 0;
        for (int valor : vetor) {
            if (valor < 0) {
                cont++;
            }
        }
        return cont;
    }

    public static void main(String[] args) {

        int[] inteiros = {10, 3, 5, -90, 3, 0, -123, -3, 4, 39};

        System.out.println(quantNegativos(inteiros));

    }

}
