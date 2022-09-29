import pyautogui
import time
import Util.planilha as p
import Util.config as c


def ajustar_filial(filial):
	# inputFilial
	pyautogui.moveTo(417, 336)
	pyautogui.click()
	pyautogui.write(filial)  

	time.sleep(tempo_entre_acoes)

def concatenar_nome_produto(nome_produto):
	lista_palavras = nome_produto.split(' ')
	return f'%{lista_palavras[-1]}'

def pesquisar_produto(produto):
	nome_produto_concatenado = concatenar_nome_produto(produto)
	
	# inputProduto
	pyautogui.moveTo(660, 336)
	pyautogui.click()
	pyautogui.write(nome_produto_concatenado)

	time.sleep(tempo_entre_acoes)

	# btnPesquisar
	pyautogui.hotkey('alt', 'p')

	time.sleep(tempo_entre_acoes)

def iniciar_pesquisa_planilha(planilha):
	print('Iniciando pesquisa...')

	print(planilha.df['Produto'].values)

	for linha in planilha.df['Produto'].values:
		pesquisar_produto(linha)

def main():
	# FAZENDO LEITURA DA CONFIGURAÇÃO%A
	config_json = c.ConfigJson('config.json')

	# Configurando tempo entre ações
	global tempo_entre_acoes
	tempo_entre_acoes = config_json.get('tempoEntreAcoes')

	# FAZENDO LEITURA DA NOVO PLANILHA E LIMPANDO DADOS DA PLANILHA RESULTADO
	planilha = p.Planilha()  

	# Preenche campos de filial
	ajustar_filial(config_json.get('filial'))	

	iniciar_pesquisa_planilha(planilha)

main()