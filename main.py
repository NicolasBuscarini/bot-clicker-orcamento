import Util.config as c
import bot_orcamento as b

def main():
	# FAZENDO LEITURA DA CONFIGURAÇÃO
	config_json = c.ConfigJson('config.json')

	# Pegando dados do config.json
	tempo_entre_acoes = config_json.get('tempoEntreAcoes')
	caracteres_indesejados = config_json.get('caracteresIndesejados')
	filial = config_json.get('filial')

	try:
		bot = b.BotOrcamento(tempo_entre_acoes, caracteres_indesejados, filial)
		bot.initialize()
	except Exception as e:
		print("#"*50)
		print('Erro ao executar o bot. Verifique se o programa está aberto e tente novamente.')
		print(e)

if __name__ == '__main__':
	main()
