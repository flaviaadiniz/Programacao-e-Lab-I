// mudar os trechos com WHILE para FOR

package semana7e8;

public class WhileAndFor {

    public static void main(String[] args) {

        System.out.println("Primeiro exemplo usando WHILE: ");
        int x = 10;
        while(x < 100){
            System.out.println(x);
            x++;
        }

        System.out.println("\nPrimeiro exemplo usando FOR: ");
        for (int i = 10; i < 100; i++) {
            System.out.println(i);
        }


        System.out.println("Segundo exemplo usando WHILE: ");
        int y = 100;
        while(y >= 0)
            System.out.println(y--);

        System.out.println("\nSegundo exemplo usando FOR: ");
        for (int i = 100; i >= 0; i--) {
            System.out.println(i);
        }


        System.out.println("Terceiro exemplo usando WHILE: ");
        int z = 50;
        while(z != 10) {
            if(z > 10) {
                z--;
                System.out.println(z);
            } else {
                z++;
                System.out.println(z);
            }
        }

        System.out.println("\nTerceiro exemplo usando FOR: ");
        for (int i = 50; i != 10;) {
            if (i > 10) {
                i--;
                System.out.println(i);
            } else {
                i++;
                System.out.println(i);
            }
        }

    }

}
