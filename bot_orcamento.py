import pyautogui
import pyperclip
import time
import Util.planilha as p
import Util.config as c

class BotOrcamento:
    def __init__(self, tempo_entre_acoes, caracteres_indesejados, filial):
        self.tempo_entre_acoes = tempo_entre_acoes
        self.caracteres_indesejados = caracteres_indesejados
        self.filial = filial

    def initialize(self):
        '''
            Executa o bot de orçamento
        '''
        # TROCA DE JANELA DO WINDOWS
        self.alt_tab()

        # FAZENDO LEITURA DA NOVO PLANILHA E LIMPANDO DADOS DA PLANILHA RESULTADO
        planilha = p.Planilha()  

        # Preenche campos de filial
        self.ajustar_filial(self.filial)	

        self.iniciar_pesquisa_planilha(planilha)
        
    def alt_tab(self):
        pyautogui.hotkey('alt', 'tab')

    def get_clipboard(self):
        '''
            Copia o texto do clipboard
        '''
        pyautogui.hotkey('ctrl', 'c')
        return pyperclip.paste()

    def ajustar_filial(self, filial : str):
        '''
            Ajusta a filial na tela do sistema
        '''
        # inputFilial
        pyautogui.moveTo(417, 336)
        pyautogui.click()
        pyautogui.write(filial)  

        time.sleep(self.tempo_entre_acoes)

    def remover_caracteres_indesejados(self, nome_produto : str, caracteres_indesejados : str):
        ''''
            Remove caracteres indesejados do nome do produto
        '''
        if caracteres_indesejados != '':
            for caracter in caracteres_indesejados:
                nome_produto = nome_produto.replace(caracter, '')
        return nome_produto

    def concatenar_nome_produto(self, nome_produto : str, caracteres_indesejados : str):
        '''
            Concatena o nome do produto com '%' entre as palavras para realizar pesquisa
        '''
        self.remover_caracteres_indesejados(nome_produto, caracteres_indesejados)

        produto_concatenado = nome_produto.replace(' ', '%')
        return produto_concatenado

    def pesquisar_produto(self, produto : str, caracteres_indesejados : str):
        '''
            Pesquisa o produto na tela do sistema
        '''
        nome_produto_concatenado = self.concatenar_nome_produto(produto, caracteres_indesejados)
        
        # inputProduto
        pyautogui.moveTo(660, 336)
        pyautogui.click()
        pyautogui.write(nome_produto_concatenado)

        time.sleep(self.tempo_entre_acoes)

        # btnPesquisar
        pyautogui.hotkey('alt', 'p')

        time.sleep(self.tempo_entre_acoes)

    def iniciar_pesquisa_planilha(self, planilha: p.Planilha):
        '''
            Inicia a pesquisa na planilha de cada produto
        '''
        print('Iniciando pesquisa...')

        for linha in planilha.df['Produto'].values:
            self.pesquisar_produto(linha, self.caracteres_indesejados)

