package semana13e14.biblioteca;

public class Principal {

    public static void main(String[] args) {


        Biblioteca biblioteca = new Biblioteca((int) (Math.random() * 201));

        for (int i = 0; i < biblioteca.getLivros().length; i++) {
            int random = (int)(Math.random() * 3);
            if (random == 1) {
                biblioteca.getLivros()[i] = new Novo();
            } else {
                biblioteca.getLivros()[i] = new Antigo();
            }
        }

        for (Livro l : biblioteca.getLivros()) {
            System.out.println(l);
        }



    }

}
