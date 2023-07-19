from analizadorLexico import analizador  # Importar el analizador léxico
import ply.lex as lex

def main():
    # Código fuente para probar el analizador léxico
    codigo_fuente = """
    #include <iostream>
    using namespace std;

    int main() {
        int x = 5;
        double y = 10.5;
        if (x > 0) {
            cout << "x es positivo" << endl;
        } else {
            cout << "x es negativo" << endl;
        }
        return 0;
    }
    """

    # Construir el analizador léxico
    lexer = lex.lex(module=analizador)

    # Asignar el código fuente al analizador léxico
    lexer.input(codigo_fuente)

    # Imprimir los tokens reconocidos
    for tok in lexer:
        print(tok)

if __name__ == "__main__":
    main()
