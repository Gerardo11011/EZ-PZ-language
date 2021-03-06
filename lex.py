# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934

import ply.lex as lex
import ply.yacc as yacc
import sys

archivo = None

# Lista de palabras reservadas.
reserved = {
    'begin': 'BEGIN',
    'end': 'END',
    'main': 'MAIN',
    'if': 'IF',
    'else': 'ELSE',
    'loop': 'LOOP',
    'func': 'FUNC',
    'int': 'INT',
    'float': 'FLOAT',
    'string': 'STRING',
    'bool': 'BOOL',
    'input': 'INPUT',
    'output': 'OUTPUT',
    'return': 'RETURN',
    'true': 'TRUE',
    'false': 'FALSE',
    'and': 'AND',
    'or': 'OR',
    'void': 'VOID'
}

# Lista de Tokens.
tokens = [

    'PLUS',
    'MINUS',
    'MULT',
    'DIV',

    'EQUAL',
    'DOUBLEEQUAL',
    'GT',
    'GTE',
    'LT',
    'LTE',
    'NE',

    'SEMICOLON',
    'COMMA',
    'LKEY',
    'RKEY',
    'LPAREN',
    'RPAREN',
    'LCORCH',
    'RCORCH',

    'CTE_S',
    'CTE_I',
    'CTE_F',

    'ID'

]


# Declaración de Tokens.
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'

t_EQUAL = r'\='
t_DOUBLEEQUAL = r'\=='
t_GT = r'\>'
t_GTE = r'\>='
t_LT = r'\<'
t_LTE = r'\<='
t_NE = r'\<>'

t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_LKEY = r'\{'
t_RKEY = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCORCH = r'\['
t_RCORCH = r'\]'

t_CTE_S = r'\"([^\\\n]|(\\.))*?\"'

tokens += list(reserved.values())


# Ignorar caracteres especiales.
t_ignore = ' \t\n'


# Declaración de funciones.
def t_CTE_F(t):
    r'[+-]?\d+\.\d+'
    t.value = float(t.value)
    return t


def t_CTE_I(t):
    r'[+-]?\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z][a-zA-Z]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_error(t):
    print("Illegal character")
    t.lexer.skip(1)


# Construir lexer.
lexer = lex.lex()

# Leer archivo de prueba.
prueba = open('Pruebas/idecode.txt', "r")
archivo = 'Pruebas/idecode.txt'
entrada = prueba.read()


# Entrada del lexer.
lexer.input(entrada)

# Mostrar tokens.
while True:
    tok = lexer.token()
    if not tok:
        break
    # print(tok)
