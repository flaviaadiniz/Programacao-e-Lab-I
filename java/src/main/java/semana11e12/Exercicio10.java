package semana11e12;

public class Exercicio10 {

    public static void main(String[] args) {

        int[] valores = {1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 6};

        System.out.println(metodo(valores));

        for(int i=0; i<valores.length; i++) {
            if(i % 2 == 0) {
                System.out.print(valores[i++] + " ");
            } else {
                System.out.print(valores[i--]+" ");
            }
        }

        System.out.println();

        System.out.println(metodo2(valores, 6));


    }

    public static int metodo(int[] array) {
        int x = 0;
        for (int i = 1; i < array.length; i++) {
            if (array[i] > array[x]) {
                x = i;
            }
        }
        return x;
    }

    public static int metodo2(int[] a, int x) {
        int z = 0;
        for (int i = 0; i < a.length; i++) {
            if (a[i] == x) {
                z++;
            }
        }
        return z;
    }

}
