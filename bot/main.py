import Util.json_util as c
import Service.bot_orcamento as b
from interfaceusuario import InterfaceUsuario


def main():
	# FAZENDO LEITURA DA CONFIGURAÇÃO
	config_json = c.Json('Config/config.json')

	# FAZENDO LEITURA DO DICIONARIO DE PRODUTOS
	dicionario_produtos = c.Json('Config/dicionario.json')

	# Pegando dados do config.json
	componentes = config_json.get('componentes')
	tempo_entre_acoes = config_json.get('tempoEntreAcoes')
	caracteres_indesejados = config_json.get('caracteresIndesejados')
	filial = config_json.get('filial')

	InterfaceUsuario.initial()

	# INICIANDO BOT
	try:
		bot = b.BotOrcamento(componentes, tempo_entre_acoes, caracteres_indesejados, filial, dicionario_produtos)
		bot.initialize()
	except Exception as e:
		InterfaceUsuario.error(e)
		print("#"*50)
		print('Erro ao executar o bot. Verifique se o programa está aberto e tente novamente.')
		print(e)


if __name__ == '__main__':
	main()
