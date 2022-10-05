import pandas as pd

class Planilha : 
    def __init__(self) :
        '''
            Inicializa a planilha leitura da tabela Execucao e limpa tabela de Resultado criando uma nova
        '''
        self.PATH_RESULTADO = 'Excel/Resultado.xlsx'
        self.PATH_EXECUCAO = 'Excel/Execucao.xlsx'             

        self.df = self.ler_dados() 
        self.criar_nova_tabela_resultado() 

    def ler_dados(self) :
        '''
            Lê os dados da tabela Execucao
        '''
        df = pd.read_excel(self.PATH_EXECUCAO)
        return df  

    def get_nome_produto(self, indice) :
        '''
            Retorna o nome do produto de acordo com o indice
        '''
        return self.df.loc[indice, "Produto"]

    def get_quantidade_produto(self, indice) :
        '''
            Retorna a quantidade do produto de acordo com o indice
        '''
        return self.df.loc[indice, "Quantidade"]

    def criar_nova_tabela_resultado(self) :
        '''
            Cria uma nova tabela de Resultado
        '''
        try:
            self.headers = {
                'Produto':[],
                'Qtd':[],
                'Encontrou':[],
                'NomeEncontrado': []
            }
            self.resultado = pd.DataFrame(self.headers)
            self.resultado.to_excel(self.PATH_RESULTADO)
        except PermissionError as e:
            print("#"*50)
            print("Permissão para editar o arquivo negada. Feche o arquivo e tente novamente.")
            print(e)

    def adicionar_dados_tabela_resultado(self, produto, qtd, encontrou, nome_encontrado = '') :
        '''
            Adiciona os dados na tabela de Resultado
        '''
        try :
            self.resultado.loc[len(self.resultado)] = [produto, qtd, encontrou, nome_encontrado]
            self.resultado.to_excel(self.PATH_RESULTADO)
        except PermissionError as e:
            print("#"*50)
            print("Permissão para editar o arquivo negada. Feche o arquivo e tente novamente.")
            print(e)
    
    def gerar_tabela_resultado(self):
        '''
            Gera tabela resultado
        '''
        self.resultado.to_excel(self.PATH_RESULTADO)