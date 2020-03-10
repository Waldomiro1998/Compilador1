from sys import exit
from analisadorLexico import *

def decVar():
	global index,indexTs,aux	
	if(tokens[index]=='TOKEN_VAR'):
		index+=1
		while(True):
			if(tokens[index]=='TOKEN_ID' and tokens[index+1]=='TOKEN_COMMA'):
				add(tokensId[indexTs])
				indexTs+=1
				index+=2
			elif(tokens[index]=='TOKEN_ID'):
				add(tokensId[indexTs])
				indexTs+=1
				index+=1
				if(tokens[index]=='TOKEN_DOT2'):
					index+=1
					if(tokens[index]=='TOKEN_REAL' or tokens[index]=='TOKEN_INTEGER'):
						if(tokens[index]=='TOKEN_REAL'):
							for x in range(0,aux):
								addType("real")
							aux=0
						elif(tokens[index]=='TOKEN_INTEGER'):
							for x in range(0,aux):
								addType("integer")
							aux=0

						index+=1
						if(tokens[index]=='TOKEN_SEMICOLON'):
							index+=1
						elif(tokens[index]=='TOKEN_IF' or tokens[index]=='TOKEN_ID'):
							break
						else:
							print("\nErro de Sintaxe Linha {}:\nEsperava comandos de atribuição ou condicional ou ';'  mas encontrou {}\n".format(
							linhas[index],tokens[index]
							))
							exit(0)		
					else:
						print("\nErro de Sintaxe Linha {}:\nEsperava um tipo 'real' ou 'integer' mas encontrou {}\n".format(
						linhas[index],tokens[index]
						))
						exit(0)
				else:
					print("\nErro de Sintaxe Linha {}:\nEsperava ':' mas encontrou {}\n".format(
					linhas[index],tokens[index]
					))
					exit(0)		
			else:
				break
	else:
		print("\nErro de Sintaxe Linha {}:\nEsperava a palavra reservada 'var' mas encontrou {}\n".format(
		linhas[index],tokens[index]
		))
		exit(0)							
def decCond():
	global index,indexTs,pilha
	while(True):
		if(tokens[index]=='TOKEN_IF'):
			index+=1
			decExp()
			if(len(list(set(pilha)))>1):
				print("Erro na linha {}, a expressão esperava um valor do tipo {}".format(linhas[index],pilha[0]))
				exit(0) 
			else:       
				pilha=[]
			if(tokens[index]=='TOKEN_THEN' ):
				index+=1
			else:
				print("\nErro de Sintaxe Linha {}:\nEsperava 'then' mas encontrou {}\n".format(
				linhas[index],tokens[index]
				))
				exit(0)
				break			
		else:			
			break	
	try:
		if(tokens[index]=='TOKEN_ID' and tokens[index+1]=='TOKEN_ASSIGNMENT' and tokens[index+2]=='TOKEN_ID'):
			pilha=[]
			checkTs(tokensId[indexTs])
			indexTs+=1
			checkTs(tokensId[indexTs])
			indexTs+=1
			if(len(list(set(pilha)))>1):
				print("Erro na linha {}, a variavel '{}'  esperava um valor do tipo {}".format(linhas[index],tokensId[indexTs-2],pilha[0]))
				exit(0) 
			else:       
				pilha=[]
			index+=3
		else:
			index+=1
			print("\nErro de Sintaxe Linha {}:\nEsperava um comando de atribuição mas encontrou {}\n".format(
			linhas[index],tokens[index]
			))
			exit(0)		
	except IndexError:
			print("\nErro de Sintaxe Linha {}:\nComando incompleto \n".format(
			linhas[index]
			))
			exit(0)						
def decExp():
	global index,indexTs
	if(tokens[index]!='TOKEN_ID'):
		print("\nErro de Sintaxe Linha {}:\nEsperava uma expressão mas encontrou {}\n".format(
		linhas[index],tokens[index]
		))
		exit(0)
	while(tokens[index]=='TOKEN_ID'):
		checkTs(tokensId[indexTs])
		indexTs+=1
		index+=1
		if(tokens[index]=='TOKEN_OPSUM'):
			index+=1
			if(tokens[index]!='TOKEN_ID'):
				print("\nErro de Sintaxe Linha {}:\nEsperava um operador no lado direito do '+' mas encontrou {}\n".format(
				linhas[index],tokens[index]
				))
				exit(0)
		else:
			break	
def analisar():
	decVar()
	checkD()
	decCond()


def add(token):
    global Ts,aux
    aux+=1
    Ts.append(token)
def addType(varType):
    global TsType
    TsType.append(varType)
def checkTs(token):
    global tokensId,Ts,linhas,posi
    if not(token in Ts):
        print("\n Erro, a variavel {} na linha {} não foi declarada".format(token,linhas[posi]))
        exit(0)
    else:
        i=Ts.index(token)    
        pilha.append(TsType[i])
def checkD():
    global Ts,linhas,index
    if len(Ts) == len(set(Ts)):
        return ""
    else:
        print("\nErro de Sintaxe na linha {}:\nTentativa de declarar uma variavel já declarada\n  ".format(linhas[index-1]))
        exit(0)

index=0
Ts=[]
TsType=[]
pilha=[]
aux=0
indexTs=0
