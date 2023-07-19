import ply.lex as lex

# Lista de tokens
tokens = (
    'ID',
    'NUM',
    'IF',
    'ELSE',
    'WHILE',
    'FOR',
    'DO',
    'SWITCH',
    'CASE',
    'BREAK',
    'CONTINUE',
    'RETURN',
    'INT',
    'DOUBLE',
    'CHAR',
    'BOOL',
    'VOID',
    'CLASS',
    'STRUCT',
    'ENUM',
    'TYPEDEF',
    'CONST',
    'STATIC',
    'NAMESPACE',
    'USING',
    'STD',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'COMMA',
)


# Reglas para tokens
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_FOR = r'for'
t_DO = r'do'
t_SWITCH = r'switch'
t_CASE = r'case'
t_BREAK = r'break'
t_CONTINUE = r'continue'
t_RETURN = r'return'
t_INT = r'int'
t_DOUBLE = r'double'
t_CHAR = r'char'
t_BOOL = r'bool'
t_VOID = r'void'
t_CLASS = r'class'
t_STRUCT = r'struct'
t_ENUM = r'enum'
t_TYPEDEF = r'typedef'
t_CONST = r'const'
t_STATIC = r'static'
t_NAMESPACE = r'namespace'
t_USING = r'using'
t_STD = r'std'

# Regla para identificadores (ID)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Regla para números enteros (NUM)
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios y saltos de línea
t_ignore = ' \n\t'

# Símbolos de puntuación
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_COMMA = r','

# Manejo de errores léxicos
def t_error(t):
    print("Carácter no válido:", t.value[0])
    t.lexer.skip(1)

# Palabras reservadas
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'do': 'DO',
    'switch': 'SWITCH',
    'case': 'CASE',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    'int': 'INT',
    'double': 'DOUBLE',
    'char': 'CHAR',
    'bool': 'BOOL',
    'void': 'VOID',
    'class': 'CLASS',
    'struct': 'STRUCT',
    'enum': 'ENUM',
    'typedef': 'TYPEDEF',
    'const': 'CONST',
    'static': 'STATIC',
    'namespace': 'NAMESPACE',
    'using': 'USING',
    'std': 'STD',
}
