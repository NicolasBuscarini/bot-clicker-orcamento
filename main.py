import pyautogui
import time
import Util.planilha as p
import Util.config as c

def alt_tab():
	pyautogui.hotkey('alt', 'tab')

def ajustar_filial(filial : str):
	'''
		Ajusta a filial na tela do sistema
	'''
	# inputFilial
	pyautogui.moveTo(417, 336)
	pyautogui.click()
	pyautogui.write(filial)  

	time.sleep(tempo_entre_acoes)

def concatenar_nome_produto(nome_produto):
	'''
		Concatena o nome do produto com '%' no começo para realizar pesquisa
	'''
	lista_palavras = nome_produto.split(' ')
	return f'%{lista_palavras[-1]}'

def pesquisar_produto(produto):
	'''
		Pesquisa o produto na tela do sistema
	'''
	nome_produto_concatenado = concatenar_nome_produto(produto)
	
	# inputProduto
	pyautogui.moveTo(660, 336)
	pyautogui.click()
	pyautogui.write(nome_produto_concatenado)

	time.sleep(tempo_entre_acoes)

	# btnPesquisar
	pyautogui.hotkey('alt', 'p')

	time.sleep(tempo_entre_acoes)

def iniciar_pesquisa_planilha(planilha: p.Planilha):
	'''
		Inicia a pesquisa na planilha de cada produto
	'''
	print('Iniciando pesquisa...')

	for linha in planilha.df['Produto'].values:
		pesquisar_produto(linha)

def bot_orcamento(config_json : c.ConfigJson):
	'''
		Executa o bot de orçamento
	'''
	# TROCA DE JANELA DO WINDOWS
	alt_tab()

	# FAZENDO LEITURA DA NOVO PLANILHA E LIMPANDO DADOS DA PLANILHA RESULTADO
	planilha = p.Planilha()  

	# Preenche campos de filial
	ajustar_filial(config_json.get('filial'))	

	iniciar_pesquisa_planilha(planilha)

def main():
	# FAZENDO LEITURA DA CONFIGURAÇÃO%A
	config_json = c.ConfigJson('config.json')

	# Configurando tempo entre ações
	global tempo_entre_acoes
	tempo_entre_acoes = config_json.get('tempoEntreAcoes')

	try:
		bot_orcamento(config_json)
	except Exception as e:
		print("#"*50)
		print('Erro ao executar o bot. Verifique se o programa está aberto e tente novamente.')
		print(e)


main()