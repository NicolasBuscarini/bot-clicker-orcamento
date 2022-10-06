import time

import pyautogui
import pygetwindow
import pyperclip

from bot.Model.componentes import Componentes
from bot.Service.planilha import Planilha
from bot.Util.json_util import JsonUtil


class BotOrcamento:
    def __init__(self, componentes, tempo_entre_acoes: float, caracteres_indesejados: str, filial: str,
                 dicionario_produtos: JsonUtil):
        self.COMPONENTES = Componentes(componentes)
        self.TEMPO_ENTRE_ACOES = tempo_entre_acoes
        self.CARACTERES_INDESEJADOS = caracteres_indesejados
        self.FILIAL = filial
        self.DICIONARIO_PRODUTOS = dicionario_produtos
        self.planilha = Planilha()

        self.produto_atual = 'null'
        self.descricao_atual = 'null'
        self.produto_anterior = 'null'

    def initialize(self):
        """
            Executa o bot de orçamento
        """
        # TROCA DE JANELA DO WINDOWS
        try:
            pygetwindow.getWindowsWithTitle('PROTHEUS')[0].activate()
        except IndexError:
            raise IndexError('Não foi possível encontrar a janela do PROTHEUS. Verifique se a janela está aberta.')
        # self.alt_tab()

        # Preenche campos de filial
        self.ajustar_filial()

        self.iniciar_pesquisa_planilha(self.planilha)

    @staticmethod
    def get_clipboard():
        """
            Copia o texto do clipboard
        """
        pyautogui.hotkey('ctrl', 'c')
        return pyperclip.paste()

    def ajustar_filial(self):
        """
            Ajusta a filial na tela do sistema
        """
        # inputFilial
        pyautogui.moveTo(self.COMPONENTES.input_filial['x'], self.COMPONENTES.input_filial['y'])
        pyautogui.click()
        pyautogui.click()
        pyautogui.write(self.FILIAL)

        time.sleep(self.TEMPO_ENTRE_ACOES)

    def converter_dicionario(self, produto: str):
        """'
            converte com o dicionario de nome de produtos
        """
        resultado_dicionario = self.DICIONARIO_PRODUTOS.get(produto)
        return resultado_dicionario

    def pesquisar_produto(self, produto: str, caracteres_indesejados: str):
        """
            Pesquisa o produto na tela do sistema
        """

        def format_nome_produto(nome_produto: str, indesejados_caracteres: str):
            """
                Remover caracteres indesejados
                Concatena o nome do produto com '%' entre as palavras para realizar pesquisa\n
                Transforma em UPPER CASE\n
            """

            def remover_caracteres_indesejados(txt: str, indesejados: str):
                """'
                    Remove caracteres indesejados do nome do produto
                """
                if indesejados != '':
                    for caracter in indesejados:
                        txt = txt.replace(caracter, '')
                return txt

            nome_produto = remover_caracteres_indesejados(nome_produto, indesejados_caracteres)

            nome_produto = nome_produto.upper()

            result = nome_produto.replace(" ", "%")

            return result

        produto = self.converter_dicionario(produto)
        nome_produto_concatenado = format_nome_produto(produto, caracteres_indesejados)

        # inputProduto
        pyautogui.moveTo(self.COMPONENTES.input_descricao['x'], self.COMPONENTES.input_descricao['y'])
        pyautogui.click()
        pyautogui.click()
        pyautogui.write(nome_produto_concatenado)

        # btnPesquisar
        pyautogui.hotkey('alt', 'p')

        time.sleep(self.TEMPO_ENTRE_ACOES)

    def iniciar_pesquisa_planilha(self, planilha: Planilha):
        """
            Inicia a pesquisa na planilha de cada produto
        """
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
        """
            Seleciona o campo de descrição
        """
        pyautogui.moveTo(self.COMPONENTES.column_descricao['x'], self.COMPONENTES.column_descricao['y'])
        pyautogui.click()

    def verificar_busca(self, produto_planilha: str, qtd_planilha: float) -> bool:
        """
            Função recursiva que verifica se o produto pesquisado é o mesmo que está na planilha
        """

        def selecionar_produto():
            """
                Seleciona o produto na tela do sistema
            """
            pyautogui.hotkey('left')
            pyautogui.hotkey('left')
            pyautogui.hotkey('left')
            pyautogui.hotkey('enter')
            pyautogui.hotkey('alt', 's')

        self.descricao_atual = BotOrcamento.get_clipboard()
        pyautogui.hotkey('left')
        self.produto_atual = BotOrcamento.get_clipboard()

        if self.produto_atual == self.produto_anterior or self.produto_atual == '' or self.produto_atual is None:
            self.planilha.adicionar_dados_tabela_resultado(produto_planilha, qtd_planilha, False)
            return False

        if self.produto_atual != self.produto_anterior:
            if not self.encontrar_produto_quantidade_menor():
                return False

            selecionar_produto()
            time.sleep(self.TEMPO_ENTRE_ACOES)

            self.produto_anterior = self.produto_atual

            self.planilha.adicionar_dados_tabela_resultado(produto_planilha, qtd_planilha, True, self.descricao_atual)
            return True

        pyautogui.hotkey('down')
        self.verificar_busca(produto_planilha, qtd_planilha)

    def encontrar_produto_quantidade_menor(self, index: int = 0, anterior: str = "null", contador_repetidos=0,
                                           dict_menor_valor: dict = None):
        """
            procura o produto com quantidade menor
        """
        # passou por todos os produtos e vai selecionar com a menor quantidade
        if contador_repetidos == 6:
            for _ in range(0, index + 1):
                pyautogui.hotkey('up')
            for _ in range(0, dict_menor_valor[0]):
                pyautogui.hotkey('down')
            return True

        if dict_menor_valor is None:
            dict_menor_valor = dict()

        clipboard = BotOrcamento.get_clipboard()

        if clipboard == "" or clipboard is None:
            print('Algo deu errado, não foi possível encontrar o produto com menor quantidade. Favor revisar.')
            return False

        if clipboard == anterior and contador_repetidos < 6:
            pyautogui.hotkey('down')
            index += 1
            contador_repetidos += 1
            self.encontrar_produto_quantidade_menor(index, clipboard, contador_repetidos)

        p = clipboard.split('.')
        qtd = int(p[1])
        if qtd < dict_menor_valor[1]:
            dict_menor_valor[0] = index
            dict_menor_valor[1] = qtd

        pyautogui.hotkey('down')
        self.encontrar_produto_quantidade_menor(index, clipboard, 0)
