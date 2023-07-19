# inter/reglasLexicasSintacticas.py

# Importar ply.lex y ply.yacc
import ply.lex as lex
import ply.yacc as yacc

# Importar los tokens necesarios del módulo tokens.py
from analizadorLexico.tokenizador import tokens

# Importar las reglas léxicas desde el archivo analizador.py
from analizadorLexico.analizador import lexer

# Importar las reglas gramaticales desde el archivo gramatica.py
from analizadorSintactico.gramatica import *

# Construir el analizador léxico
lexer = lex.lex(module=lexer)

# Construir el analizador sintáctico
parser = yacc.yacc()

# Función para analizar una cadena de entrada
def analizar_cadena(cadena):
    resultado = parser.parse(cadena, lexer=lexer)
    return resultado

# Reglas léxicas y sintácticas adicionales para C++
def p_funcion(p):
    '''
    funcion : tipo ID LPAREN RPAREN LBRACE RBRACE
    '''
    print("Declaración de función:", p[1], p[2])

def p_if_statement(p):
    '''
    if_statement : IF LPAREN expresion RPAREN LBRACE RBRACE
                 | IF LPAREN expresion RPAREN LBRACE RBRACE ELSE LBRACE RBRACE
    '''
    print("Sentencia if:", p[3])
def p_bucle_while(p):
    '''
    bucle_while : WHILE LPAREN expresion RPAREN LBRACE sentencias RBRACE
    '''
    print("Bucle while:", p[3])

def p_bucle_for(p):
    '''
    bucle_for : FOR LPAREN expresion_opt SEMICOLON expresion_opt SEMICOLON expresion_opt RPAREN LBRACE sentencias RBRACE
    '''
    print("Bucle for")

def p_expresion_opt(p):
    '''
    expresion_opt : expresion
                  |
    '''
    pass

def p_sentencias(p):
    '''
    sentencias : sentencia
               | sentencias sentencia
    '''
    pass

def p_sentencia(p):
    '''
    sentencia : bucle_while
              | bucle_for
              | if_statement
              | declaracion
              | asignacion
              | expresion SEMICOLON
              | RETURN expresion SEMICOLON
              | BREAK SEMICOLON
              | CONTINUE SEMICOLON
    '''
    pass
def p_funcion(p):
    '''
    funcion : tipo ID LPAREN parametros_opt RPAREN LBRACE sentencias RBRACE
    '''
    print("Declaración de función:", p[1], p[2])

def p_parametros_opt(p):
    '''
    parametros_opt : parametros
                   |
    '''
    pass

def p_parametros(p):
    '''
    parametros : parametro
               | parametros COMMA parametro
    '''
    pass

def p_parametro(p):
    '''
    parametro : tipo ID
    '''
    pass

def p_tipo(p):
    '''
    tipo : INT
         | DOUBLE
         | CHAR
         | BOOL
         | VOID
    '''
    pass

def p_switch(p):
    '''
    switch : SWITCH LPAREN expresion RPAREN LBRACE casos RBRACE
    '''
    print("Estructura switch")

def p_casos(p):
    '''
    casos : caso
          | casos caso
    '''
    pass

def p_caso(p):
    '''
    caso : CASE expresion COLON sentencias
         | DEFAULT COLON sentencias
    '''
    pass
