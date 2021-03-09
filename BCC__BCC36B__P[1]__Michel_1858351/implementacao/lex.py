# -*- coding: utf-8 -*-
chave = 0
import ply.lex as lex
import sys
import re

tokens = (
'NUM_INTEIRO',
'MAIS',
'MENOS',
'MULTIPLICACAO',
'DIVISAO',
'DOIS_PONTOS',
'VIRGULA',
'MENOR',
'MAIOR',
'IGUAL',
'DIFERENTE',
'MENOR_IGUAL',
'MAIOR_IGUAL',
'E_LOGICO',
'OU_LOGICO',
'NEGACAO',
'ABRE_PARENTESE',
'FECHA_PARENTESE',
'ABRE_COLCHETE',
'FECHA_COLCHETE',
'SE',
'ENTAO',
'SENAO',
'REPITA',
'ATE',
'ATRIBUICAO',
'LEIA',
'ESCREVA',
'RETORNA',
'INTEIRO',
'FLUTUANTE',
'NUM_PONTO_FLUTUANTE',
'NUM_NOTACAO_CIENTIFICA',
'ID',
'ABRE_CHAVES',
'FIM',
'FECHA_CHAVES',
'COMENTARIO'
)

t_SE = r'(se)[^\w+]'
t_SENAO = r'(senão)'
t_ATE = r'até'
t_LEIA = r'leia'
t_ENTAO = r'então'
t_REPITA = r'repita'
t_ESCREVA = r'escreva'
t_RETORNA = r'retorna'
t_INTEIRO = r'inteiro'
t_FLUTUANTE = r'flutuante'
t_MENOR = r'<'
t_MAIOR = r'>'
t_IGUAL = r'='
t_DIVISAO = r'/'
t_VIRGULA = r','
t_NEGACAO = r'!'
t_E_LOGICO = r'&&'
t_DIFERENTE = r'<>'
t_OU_LOGICO = r'\|\|'
t_ATRIBUICAO = r':='
t_DOIS_PONTOS = r':'
t_MENOR_IGUAL = r'<='
t_MAIOR_IGUAL = r'>='
#t_COMENTARIO = r'\{[\w\n\r\s\t]+.*\}'
t_MULTIPLICACAO = r'\*'
t_ABRE_COLCHETE = r'\['
t_FECHA_COLCHETE = r'\]'
t_ABRE_PARENTESE = r'\('
t_FECHA_PARENTESE = r'\)'
t_ID = r'\w+'

t_ignore  = " \t"


def t_NUM_NOTACAO_CIENTIFICA(t):
    r'\d+\^+\d+'
    t.value = t.value    
    return t

def t_NUM_PONTO_FLUTUANTE(t):
    r'\d+\.\d*' 
    t.value = float(t.value)    
    return t
    
def t_COMENTARIO(token):
    r"(\{((.|\n)*?)\})"
    token.lexer.lineno += token.value.count("\n")
    # return token

def t_NUM_INTEIRO(t):
    r'((?<=\D)[+-]\d+)|(?<=\W)\d+'
    t.value = int(t.value)    
    return t
#https://regex101.com/r/Ebg5LT/2

def t_FIM(token):
	r'fim'
	return token

def t_MAIS(t):
    #r'\+'
    r'\+'
    return t

def t_MENOS(t):
    r'-'
    return t

#def t_error(t):
#    print("Caracter inválido '%s'" % t.value[0])
#    t.lexer.skip(1)


def t_newline(t):
	r"\n+"
	t.lexer.lineno += len(t.value)

def t_error(token):

    line = token.lineno
    message ="Caracter inválido '%s'" % token.value[0]
    print(message)
    token.lexer.skip(1)

lexer = lex.lex()

def proxToken(data):

    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok: 
            break
        if(chave == 1):
            print(tok.type, tok.value)#print(tok.type, tok.value)
        else:
            print(tok.type)

def main():
    
    f = open(sys.argv[1])
    data = str(f.read())

    proxToken(data)

if __name__ == '__main__':
    main()
