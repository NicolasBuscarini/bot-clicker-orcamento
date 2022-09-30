import pyautogui
import pyperclip
import time
import Util.planilha as p

class BotOrcamento:
    def __init__(self, tempo_entre_acoes, caracteres_indesejados, filial):
        self.TEMPO_ENTRE_ACOES = tempo_entre_acoes
        self.CARACTERES_INDESEJADOS = caracteres_indesejados
        self.FILIAL = filial

    def initialize(self):
        '''
            Executa o bot de orçamento
        '''
        # TROCA DE JANELA DO WINDOWS
        self.alt_tab()

        # FAZENDO LEITURA DA NOVO PLANILHA E LIMPANDO DADOS DA PLANILHA RESULTADO
        planilha = p.Planilha()  

        # Preenche campos de filial
        self.ajustar_filial()	

        self.iniciar_pesquisa_planilha(planilha)
        
    def alt_tab(self):
        pyautogui.hotkey('alt', 'tab')

    def get_clipboard(self):
        '''
            Copia o texto do clipboard
        '''
        pyautogui.hotkey('ctrl', 'c')
        return pyperclip.paste()

    def ajustar_filial(self):
        '''
            Ajusta a filial na tela do sistema
        '''
        # inputFilial
        pyautogui.moveTo(417, 336)
        pyautogui.click()
        pyautogui.write(self.FILIAL)  

        time.sleep(self.TEMPO_ENTRE_ACOES)

    def remover_caracteres_indesejados(self, nome_produto : str, caracteres_indesejados : str):
        ''''
            Remove caracteres indesejados do nome do produto
        '''
        if caracteres_indesejados != '':
            for caracter in caracteres_indesejados:
                nome_produto = nome_produto.replace(caracter, '')
        return nome_produto

    def format_nome_produto(self, nome_produto : str, caracteres_indesejados : str):
        '''
            Concatena o nome do produto com '%' entre as palavras para realizar pesquisa
            Transforma em UPPER CASE
        '''
        nome_produto = self.remover_caracteres_indesejados(nome_produto, caracteres_indesejados)

        nome_produto = nome_produto.upper()

        produto_formatado = nome_produto.replace(' ', '%')
        return produto_formatado

    def pesquisar_produto(self, produto : str, caracteres_indesejados : str):
        '''
            Pesquisa o produto na tela do sistema
        '''
        nome_produto_concatenado = self.format_nome_produto(produto, caracteres_indesejados)
        
        # inputProduto
        pyautogui.moveTo(660, 336)
        pyautogui.click()
        pyautogui.write(nome_produto_concatenado)

        time.sleep(self.TEMPO_ENTRE_ACOES)

        # btnPesquisar
        pyautogui.hotkey('alt', 'p')

        time.sleep(self.TEMPO_ENTRE_ACOES)

    def iniciar_pesquisa_planilha(self, planilha: p.Planilha):
        '''
            Inicia a pesquisa na planilha de cada produto
        '''
        print('Iniciando pesquisa...')

        for linha in planilha.df['Produto'].values:
            self.pesquisar_produto(linha, self.CARACTERES_INDESEJADOS)

    def selecionar_campo_descricao(self):
        '''
            Seleciona o campo de descrição
        '''
        pyautogui.moveTo(532, 404)
        pyautogui.click()

    def verificar_busca(self, produto_planilha : str, produto_anterior : str):
        '''
            Verifica se o produto foi encontrado
        '''
        self.selecionar_campo_descricao()

        descricao_produto = self.get_clipboard()

        if descricao_produto == produto_planilha:
            time.sleep(self.TEMPO_ENTRE_ACOES)
            return True
            
        if descricao_produto == produto_anterior:
            time.sleep(self.TEMPO_ENTRE_ACOES)
            return False

        pyautogui.hotkey('down')
        self.verificar_busca(produto_planilha, descricao_produto)