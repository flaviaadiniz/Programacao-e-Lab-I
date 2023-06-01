/*
Exercício 5. Crie um método que recebe um array de inteiros a e um valor inteiro x e retorna a quantidade de vezes
que x aparece no array a.
 */
package semana11e12;

public class Exercicio5 {

    public static int quantVezesXEmA(int[] a, int x) {
        int cont = 0;
        for (int valor : a) {
            if (valor == x) {
                cont++;
            }
        }
        return cont;
    }


    public static void main(String[] args) {

        int[] arrayTeste = {1, 4, 56, 23, 4, 78, 987, 4, 0};

        System.out.println(quantVezesXEmA(arrayTeste, 4));

    }
}
