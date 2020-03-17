import ply.lex as lex
import sys

tokens = (
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
'NUM_INTEIRO',
'NUM_PONTO_FLUTUANTE',
'NUM_NOTACAO_CIENTIFICA',
'ID',
'ABRE_CHAVES',
'FECHA_CHAVES',
'COMENTARIO'
)


def t_NUM_INTEIRO(t):
    #r'\d+$'
    #r'^(\d)|(-\d)'

    #r'^(\d)|((\s|\t|\n)?-\d)'

   
    #r'[^(\d+)(\+|\-)(\d+)]([^(:=\s)][-]\d+)|(\d+)'
    
    
    #r'([^(\d+)\-(\d+)]([-]\d+))'
    r'([^(\d+)]?([-]?\d+))[^(\d+)\-(\d+)]'
    
    
    #r'[^(\d+)(\+|\-)(\d+)](-\d+)|(\d+)'
    #r'(^(\+|-)?(\d+))' reconhece só o d+
    #r'(^(-|\+)?(\d+$))'

    #r'((\s|\t|\n)-\d)'
    #t.value = t.value.replace(":=","")

    t.value = int(t.value)    
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