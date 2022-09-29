import pyautogui
import time
import planilha as p

pyautogui.click()
pyautogui.moveTo(0, 0)

def load_images(lst):
	imgs = {}
	
	for name in lst:
		if type(name) is tuple:
			path = f"{IMGS_DIR}{name[0]}.jpg"
			if len(name) > 1:
				pag = name[1]
			if len(name) > 2:
				precision = name[2]
			imgs[name] = Search(path, pag=pag, precision=precision)
		else:
			path = f"{IMGS_DIR}{name}.jpg"
			imgs[name] = Search(path)
	
	return imgs


def main() :
    planilha = p.Planilha()
    planilha.criar_nova_tabela_resultado()

    nome_produto = planilha.get_nome_produto(7)
    qtd = planilha.get_quantidade_produto(7)
    planilha.adicionar_dados_tabela_resultado(nome_produto, qtd, True)

    nome_produto = planilha.get_nome_produto(3)
    qtd = planilha.get_quantidade_produto(3)
    planilha.adicionar_dados_tabela_resultado(nome_produto, qtd, True)

main()