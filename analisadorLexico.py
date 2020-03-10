import re 
def tokenTranslate(token):
	global linha
	if(token=='var'):
		return 'TOKEN.VAR'
	elif(token=='integer'):
		return 'TOKEN.INTEGER'	
	elif(token=='real'):
		return 'TOKEN.REAL'
	elif(token=='if'):
		return 'TOKEN.IF'
	elif(token=='then'):
		return 'TOKEN.THEN'
	elif(token==':'):
		return 'TOKEN.DOT2'						
	elif(token==','):
		return 'TOKEN.COMMA'		
	elif(token==';'):
		return 'TOKEN.SEMICOLON'
	elif(token==':='):
		return 'TOKEN.ASSIGNMENT'
	elif(token=='+'):
		return 'TOKEN.OPSUM'
	else:							
		if (token.isalnum() and token[0].isalpha()):
			tokensId.append(token)
			return 'TOKEN.ID'
		else:
			erros.append((linha, token))
def tokenizar(arquivo):
	global linha
	arquivo =re.split(r'(;|,|:=|:|\n|[^a-z0-9])',arquivo)
	while("" in arquivo): 
		arquivo.remove("")
	while(" " in arquivo): 
		arquivo.remove(" ")  
	for palavra in arquivo:
		if palavra == '\n':
			linha += 1
		elif palavra != "":
			tokens.append(tokenTranslate(palavra))
			linhas.append(linha)
	if len(erros) > 0:
		erro = ''
		for i in erros:
			erro += "Erro Léxico, Linha {}: Não é valído o identificador {} \n".format(i[0], i[1])
		print(erro)
tokens,erros, tokensId,linhas = [], [], [], []
linha=1
