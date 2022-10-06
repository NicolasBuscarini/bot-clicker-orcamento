from bot.Service.bot_orcamento import BotOrcamento
from bot.Util.json_util import JsonUtil
from bot.interfaceusuario import InterfaceUsuario


def main():
	# FAZENDO LEITURA DA CONFIGURAÇÃO
	config_json = JsonUtil('Config/config.json')

	# FAZENDO LEITURA DO DICIONARIO DE PRODUTOS
	dicionario_produtos = JsonUtil('Config/dicionario.json')

	# Pegando dados do config.json
	componentes = config_json.get('componentes')
	tempo_entre_acoes = config_json.get('tempoEntreAcoes')
	caracteres_indesejados = config_json.get('caracteresIndesejados')
	filial = config_json.get('filial')

	InterfaceUsuario.initial()

	# INICIANDO BOT
	try:
		bot = BotOrcamento(componentes, tempo_entre_acoes, caracteres_indesejados, filial, dicionario_produtos)
		bot.initialize()
	except Exception as e:
		InterfaceUsuario.error(e)
		print("#"*50)
		print('Erro ao executar o bot. Verifique se o programa está aberto e tente novamente.')
		print(e)


if __name__ == '__main__':
	main()
