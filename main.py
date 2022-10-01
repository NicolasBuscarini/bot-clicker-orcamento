import Util.json as c
import bot_orcamento as b

def main():
	# FAZENDO LEITURA DA CONFIGURAÇÃO
	config_json = c.Json('config.json')

	# FAZENDO LEITURA DO DICIONARIO DE PRODUTOS
	DICIONARIO_PRODUTOS = c.Json('dicionario.json')

	# Pegando dados do config.json
	TEMPO_ENTRE_ACOES = config_json.get('tempoEntreAcoes')
	CARACTERES_INDESEJADOS = config_json.get('caracteresIndesejados')
	FILIAL = config_json.get('filial')

	try:
		bot = b.BotOrcamento(TEMPO_ENTRE_ACOES, CARACTERES_INDESEJADOS, FILIAL, DICIONARIO_PRODUTOS)
		bot.initialize()
	except Exception as e:
		print("#"*50)
		print('Erro ao executar o bot. Verifique se o programa está aberto e tente novamente.')
		print(e)

if __name__ == '__main__':
	main()
