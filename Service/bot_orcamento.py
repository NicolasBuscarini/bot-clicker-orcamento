from asyncio.windows_events import NULL
import pyautogui
import pyperclip
import time
from Model.componentes import Componentes
from Service.planilha import Planilha
from Util.json import Json

class BotOrcamento:
    def __init__(self, componentes, tempo_entre_acoes: float, caracteres_indesejados: str, filial: str, dicionario_produtos: Json):
        self.COMPONENTES = Componentes(componentes)
        self.TEMPO_ENTRE_ACOES = tempo_entre_acoes
        self.CARACTERES_INDESEJADOS = caracteres_indesejados
        self.FILIAL = filial
        self.DICIONARIO_PRODUTOS = dicionario_produtos
        self.planilha = Planilha() 

        self.produto_atual = 'null'
        self.descricao_atual = 'null'
        self.produto_anterior = 'null'
        self.descricao_anterior = 'null'

    def initialize(self):
        '''
            Executa o bot de orçamento
        '''
        # TROCA DE JANELA DO WINDOWS
        self.alt_tab()         

        # Preenche campos de filial
        self.ajustar_filial()	

        self.iniciar_pesquisa_planilha(self.planilha)
        
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
        pyautogui.moveTo(self.COMPONENTES.input_filial['x'], self.COMPONENTES.input_filial['y'])
        pyautogui.click()
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
            Remover caracteres indesejados
            Concatena o nome do produto com '%' entre as palavras para realizar pesquisa\n
            Transforma em UPPER CASE\n
        '''
        nome_produto = self.remover_caracteres_indesejados(nome_produto, caracteres_indesejados)

        nome_produto = nome_produto.upper()

        nome_produto_concatenado = nome_produto.replace(" ", "%")

        return nome_produto_concatenado

    def converter_dicionario(self, produto: str) :
        ''''
            converte com o dicionario de nome de produtos
        '''
        resultado_dicionario = self.DICIONARIO_PRODUTOS.get(produto)
        return resultado_dicionario

    def pesquisar_produto(self, produto : str, caracteres_indesejados : str):
        '''
            Pesquisa o produto na tela do sistema
        '''
        self.converter_dicionario(produto)
        nome_produto_concatenado = self.format_nome_produto(produto, caracteres_indesejados)
        
        # inputProduto
        pyautogui.moveTo(self.COMPONENTES.input_descricao['x'], self.COMPONENTES.input_descricao['y'])
        pyautogui.click()
        pyautogui.click()
        pyautogui.write(nome_produto_concatenado)

        time.sleep(self.TEMPO_ENTRE_ACOES)

        # btnPesquisar
        pyautogui.hotkey('alt', 'p')

        time.sleep(self.TEMPO_ENTRE_ACOES)

    def iniciar_pesquisa_planilha(self, planilha: Planilha):
        '''
            Inicia a pesquisa na planilha de cada produto
        '''
        print('Iniciando pesquisa...')

        for linha in planilha.df.values:
            print(str('Pesquisando produto: ' + linha[0] + ' Quantidade: ') + str(linha[1]))

            self.pesquisar_produto(linha[0], self.CARACTERES_INDESEJADOS)
            self.selecionar_campo_descricao()

            if self.verificar_busca(linha[0], linha[1]):
                print(f'Produto {linha[0]} encontrado!')
            else:
                print(f'Produto {linha[0]} não encontrado!')

        print('Pesquisa finalizada!')

    def selecionar_campo_descricao(self):
        '''
            Seleciona o campo de descrição
        '''
        pyautogui.moveTo(self.COMPONENTES.column_descricao['x'], self.COMPONENTES.column_descricao['y'])
        pyautogui.click()

    def verificar_busca(self, produto_planilha : str, qtd_planilha: float) -> bool:
        '''
            Função recursiva que verifica se o produto pesquisado é o mesmo que está na planilha
        '''
        self.descricao_atual = self.get_clipboard()
        pyautogui.hotkey('left')
        self.produto_atual = self.get_clipboard()
        
        if self.produto_atual == self.produto_anterior or self.produto_atual == '' or self.produto_atual == NULL:
            time.sleep(self.TEMPO_ENTRE_ACOES)
            
            self.planilha.adicionar_dados_tabela_resultado(produto_planilha, qtd_planilha, False)
            return False
        
        if self.produto_atual != self.produto_anterior :
            time.sleep(self.TEMPO_ENTRE_ACOES)
            self.selecionar_produto()
            self.produto_anterior = self.produto_atual
            self.descricao_anterior = self.descricao_atual

            self.planilha.adicionar_dados_tabela_resultado(produto_planilha, qtd_planilha, True)
            return True
            
        pyautogui.hotkey('down')
        self.verificar_busca(produto_planilha, qtd_planilha)

    def selecionar_produto(self):
        '''
            Seleciona o produto na tela do sistema
        '''
        pyautogui.hotkey('left')
        pyautogui.hotkey('left')
        pyautogui.hotkey('left')
        pyautogui.hotkey('enter')

        pyautogui.hotkey('alt', 's')

    