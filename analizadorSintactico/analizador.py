# Importar el módulo ply.lex para el analizador léxico
import ply.lex as lex

# Importar el módulo ply.yacc para el analizador sintáctico
import ply.yacc as yacc

# Importar el módulo tokens que contiene la lista de tokens y sus reglas para el analizador léxico
from token import tokens

# Importar el módulo gramatica que contiene las reglas gramaticales para el analizador sintáctico
from analizadorSintactico.gramatica import *

# Importar el módulo lexer desde el archivo analizador.py que contiene las reglas para el analizador léxico
from . import lexer

# Construir el analizador léxico
lexer = lex.lex(module=lexer)

# Construir el analizador sintáctico
parser = yacc.yacc()

# Función para analizar una cadena de entrada
def analizar_cadena(cadena):
    resultado = parser.parse(cadena, lexer=lexer)
    return resultado
