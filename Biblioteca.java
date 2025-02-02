import java.util.ArrayList;
import java.util.Scanner;

// Classe que representa um Livro
class Livro {
    private String titulo;
    private String autor;
    private int ano;

    // Construtor
    public Livro(String titulo, String autor, int ano) {
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
    }

    // Métodos Getters
    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public int getAno() {
        return ano;
    }

    // Método para exibir detalhes do livro
    public void exibirDetalhes() {
        System.out.println("Título: " + titulo + " | Autor: " + autor + " | Ano: " + ano);
    }
}

// Classe principal
public class Biblioteca {
    private static ArrayList<Livro> livros = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int opcao;

        do {
            System.out.println("\n----- Biblioteca -----");
            System.out.println("1 - Adicionar Livro");
            System.out.println("2 - Listar Livros");
            System.out.println("3 - Buscar Livro por Título");
            System.out.println("4 - Remover Livro");
            System.out.println("5 - Sair");
            System.out.print("Escolha uma opção: ");
            opcao = scanner.nextInt();
            scanner.nextLine(); // Consumir a quebra de linha

            switch (opcao) {
                case 1:
                    adicionarLivro();
                    break;
                case 2:
                    listarLivros();
                    break;
                case 3:
                    buscarLivro();
                    break;
                case 4:
                    removerLivro();
                    break;
                case 5:
                    System.out.println("Saindo do sistema...");
                    break;
                default:
                    System.out.println("Opção inválida. Tente novamente.");
            }
        } while (opcao != 5);

        scanner.close();
    }

    // Método para adicionar um livro
    private static void adicionarLivro() {
        System.out.print("Título: ");
        String titulo = scanner.nextLine();

        System.out.print("Autor: ");
        String autor = scanner.nextLine();

        System.out.print("Ano de publicação: ");
        int ano = scanner.nextInt();
        scanner.nextLine(); // Consumir a quebra de linha

        livros.add(new Livro(titulo, autor, ano));
        System.out.println("Livro adicionado com sucesso!");
    }

    // Método para listar os livros cadastrados
    private static void listarLivros() {
        if (livros.isEmpty()) {
            System.out.println("Nenhum livro cadastrado.");
        } else {
            System.out.println("\n--- Lista de Livros ---");
            for (Livro livro : livros) {
                livro.exibirDetalhes();
            }
        }
    }

    // Método para buscar um livro pelo título
    private static void buscarLivro() {
        System.out.print("Digite o título do livro: ");
        String titulo = scanner.nextLine();

        for (Livro livro : livros) {
            if (livro.getTitulo().equalsIgnoreCase(titulo)) {
                System.out.println("Livro encontrado:");
                livro.exibirDetalhes();
                return;
            }
        }
        System.out.println("Livro não encontrado.");
    }

    // Método para remover um livro pelo título
    private static void removerLivro() {
        System.out.print("Digite o título do livro a ser removido: ");
        String titulo = scanner.nextLine();

        for (Livro livro : livros) {
            if (livro.getTitulo().equalsIgnoreCase(titulo)) {
                livros.remove(livro);
                System.out.println("Livro removido com sucesso!");
                return;
            }
        }
        System.out.println("Livro não encontrado.");
    }
}
