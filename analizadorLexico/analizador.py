import ply.lex as lex
import tokenizador 

# Construir el analizador léxico
lexer = lex.lex(module=tokenizador)

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

# Asignar el código fuente al analizador léxico
lexer.input(codigo_fuente)

# Imprimir los tokens reconocidos
for tok in lexer:
    print(tok)

# Reglas para tokens de entrada y salida (COUT y CIN)
def t_COUT(t):
    r'cout'
    return t

def t_CIN(t):
    r'cin'
    return t
