# Lista de tokens de entrada y salida
tokens_entrada_salida = (
    'COUT',
    'CIN',
)

# Reglas para los tokens de entrada y salida
def t_COUT(t):
    r'cout'
    return t

def t_CIN(t):
    r'cin'
    return t
