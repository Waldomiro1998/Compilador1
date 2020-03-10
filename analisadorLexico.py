def dicAnalise(token):
    global linha
    try:
        return dic[token]
    except KeyError:
        if (token.isalnum() and token[0].isalpha()):
            tokensId.append(token)
            return 'TOKEN_ID'
        else:
            erros.append((linha, token))
def tokenizar(arquivo):
	global linha
	arquivo = arquivo.replace(':', ' : ')
	arquivo = arquivo.replace(": =", ' := ')
	arquivo = arquivo.replace('+', ' + ')
	arquivo = arquivo.replace(',', ' , ')
	arquivo = arquivo.replace(';', ' ; ')
	arquivo = arquivo.replace('\n', ' \n ')
	arquivo = arquivo.split(' ')
	for palavra in arquivo:
		if palavra == '\n':
			linha += 1
		elif palavra != "":
			tokens.append(dicAnalise(palavra))
			linhas.append(linha)
	if len(erros) > 0:
		erro = ''
		for i in erros:
			erro += "Erro Léxico, Linha {}: Não é valído o identificador {} \n".format(i[0], i[1])
		print(erro)

tokens,erros, tokensId,linhas = [], [], [], []
linha=1
dic = {'var': 'TOKEN_VAR', 'integer': 'TOKEN_INTEGER', 'real': 'TOKEN_REAL',
            'if': 'TOKEN_IF', 'then': 'TOKEN_THEN', ':': 'TOKEN_DOT2',
            ',': 'TOKEN_COMMA', ';': 'TOKEN_SEMICOLON', ':=': 'TOKEN_ASSIGNMENT',
            '+': 'TOKEN_OPSUM'}
