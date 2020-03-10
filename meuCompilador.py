from analisadorLexico import *

from analisadorSintatico import *

fd = open('arqFonte','r')
stream = fd.read()
tokenizar(stream) 
analisar()
fd.close()
