import pyautogui
import pyperclip
import time
import Util.planilha as p
import Util.config as c

def alt_tab():
	pyautogui.hotkey('alt', 'tab')

def get_clipboard():
	'''
		Copia o texto do clipboard
	'''
	pyautogui.hotkey('ctrl', 'c')
	return pyperclip.paste()

def ajustar_filial(filial : str):
	'''
		Ajusta a filial na tela do sistema
	'''
	# inputFilial
	pyautogui.moveTo(417, 336)
	pyautogui.click()
	pyautogui.write(filial)  

	time.sleep(tempo_entre_acoes)

def remover_caracteres_indesejados(nome_produto : str, caracteres_indesejados : str):
	''''
		Remove caracteres indesejados do nome do produto
	'''
	if caracteres_indesejados != '':
		for caracter in caracteres_indesejados:
			nome_produto = nome_produto.replace(caracter, '')
	return nome_produto

def concatenar_nome_produto(nome_produto : str, caracteres_indesejados : str):
	'''
		Concatena o nome do produto com '%' entre as palavras para realizar pesquisa
	'''
	remover_caracteres_indesejados(nome_produto, caracteres_indesejados)

	produto_concatenado = nome_produto.replace(' ', '%')
	return produto_concatenado

def pesquisar_produto(produto : str, caracteres_indesejados : str):
	'''
		Pesquisa o produto na tela do sistema
	'''
	nome_produto_concatenado = concatenar_nome_produto(produto, caracteres_indesejados)
	
	# inputProduto
	pyautogui.moveTo(660, 336)
	pyautogui.click()
	pyautogui.write(nome_produto_concatenado)

	time.sleep(tempo_entre_acoes)

	# btnPesquisar
	pyautogui.hotkey('alt', 'p')

	time.sleep(tempo_entre_acoes)

def iniciar_pesquisa_planilha(planilha: p.Planilha, config_json: c.ConfigJson):
	'''
		Inicia a pesquisa na planilha de cada produto
	'''
	print('Iniciando pesquisa...')

	for linha in planilha.df['Produto'].values:
		pesquisar_produto(linha, config_json.get('caracteresIndesejados'))

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

	iniciar_pesquisa_planilha(planilha, config_json)

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