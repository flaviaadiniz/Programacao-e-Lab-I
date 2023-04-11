public class Aluno {

    String nome;
    String matricula;
    double grauA;
    double grauB;

    public Aluno(String nome, String matricula, double grauA, double grauB) {
        this.nome = nome;
        this.matricula = matricula;
        this.grauA = grauA;
        this.grauB = grauB;
    }

    public double calcularMediafinal(double grauA, double grauB) {
        return (grauA * 0.33) + (grauB * 0.67);
    }

    public String imprimeInfo() {
        return "Nome do aluno: " + getNome() +
                "\nMatrícula: " + getMatricula() +
                "\nGrau A: " + getGrauA() +
                "\nGrau B: " + getGrauB() +
                "\nMédia Final: " + calcularMediafinal(getGrauA(), getGrauB());
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getMatricula() {
        return matricula;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

    public double getGrauA() {
        return grauA;
    }

    public void setGrauA(double grauA) {
        this.grauA = grauA;
    }

    public double getGrauB() {
        return grauB;
    }

    public void setGrauB(double grauB) {
        this.grauB = grauB;
    }
}
