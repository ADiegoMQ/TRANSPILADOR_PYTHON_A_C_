# Importar ply.yacc
import ply.yacc as yacc
from token import tokens

# Importar la función lexer desde analizador.py
from analizadorLexico.analizador import lexer

# Reglas gramaticales
def p_declaracion(p):
    '''
    declaracion : tipo ID SEMICOLON
    '''
    print("Declaración:", p[1], p[2])

def p_tipo(p):
    '''
    tipo : INT
         | DOUBLE
         | CHAR
    '''
    p[0] = p[1]

# Manejo de errores sintácticos
def p_error(p):
    print("Error de sintaxis:", p)

# Construir el parser
parser = yacc.yacc()

# Prueba del analizador sintáctico
while True:
    try:
        s = input("Ingrese una declaración: ")
    except EOFError:
        break
    if not s:
        continue

    # Parsear la entrada
    result = parser.parse(s, lexer=lexer)
