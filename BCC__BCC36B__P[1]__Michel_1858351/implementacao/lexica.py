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
'FIM',
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
'FECHA_CHAVES',
'COMENTARIO'
)

t_FIM = r'fim'
t_SE = r'(se)'
t_SENAO = r'(senão)'
t_ATE = r'até'
t_LEIA = r'leia'
t_ENTAO = r'então'
t_REPITA = r'repita'
t_ESCREVA = r'escreva'
t_RETORNA = r'retorna'
t_INTEIRO = r'inteiro'
t_FLUTUANTE = r'flutuante'
#t_MAIS = r'\+'
#t_MENOS = r'-'
t_MENOR = r'<'
t_MAIOR = r'>'
t_IGUAL = r'=='
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
#t_FECHA_CHAVES = r'\}'
#t_ABRE_CHAVES = r'\{'
t_COMENTARIO = r'\{[\w\n\r\s\t]+.*\}'
t_MULTIPLICACAO = r'\*'
t_ABRE_COLCHETE = r'\['
t_FECHA_COLCHETE = r'\]'
t_ABRE_PARENTESE = r'\('
t_FECHA_PARENTESE = r'\)'
t_ID = r'\w+'

def t_NUM_NOTACAO_CIENTIFICA(t):
    r'\d+\^+\d+'
    t.value = t.value    
    return t

def t_NUM_PONTO_FLUTUANTE(t):
    r'\d+\.\d*' 
    t.value = float(t.value)    
    return t
    


def t_NUM_INTEIRO(t):
    #r'\d+'
    #r'^[-+]?\d+$'
    
    #r'[^\d][-+]?\d+'


    #r'[^\d|^(][-]?\d+|[^\d+(\+)]\d+'

    #r'[^\d+|^(][-]?\d+|\d+'

    #r'((:=)?(\s)?(\+|-)?(\d+))'
    #t.value = t.value.replace(":=","")

    #r'((\D)[+-]\d+)|\d+'
    r'((?<=\D)[+-]\d+)|\d+'
    t.value = int(t.value)    
    return t

def t_MAIS(t):
    #r'\+'
    r'\+'
    return t

def t_MENOS(t):
    r'-'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print("Caractere Ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def proxToken(data):

    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok: 
            break      
        print(tok.type, tok.value)
        #print(tok.type)

def main():
    
    f = open(sys.argv[1])
    data = str(f.read())

    proxToken(data)

if __name__ == '__main__':
    main()