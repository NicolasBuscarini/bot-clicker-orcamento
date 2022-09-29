import pandas as pd

class Planilha : 
    def __init__(self) :
        self.df = self.ler_dados() 
        self.criar_nova_tabela_resultado()       

    def ler_dados(self) :
        df = pd.read_excel("Excel/teste.xlsx")
        return df  

    def get_nome_produto(self, indice) :
        return self.df.loc[indice, "Produto"]

    def get_quantidade_produto(self, indice) :
        return self.df.loc[indice, "Quantidade (g)"]

    def criar_nova_tabela_resultado(self) :
        try:
            self.headers = {
                'Produto':[],
                'Qtd':[],
                'Encontrou':[]
            }
            self.resultado = pd.DataFrame(self.headers)
            self.resultado.to_excel('resultado.xlsx')
        except PermissionError as e:
            print("#"*50)
            print("Permissão para editar o arquivo negada. Feche o arquivo e tente novamente.")
            print(e)

    def adicionar_dados_tabela_resultado(self, produto, qtd, encontrou) :
        try :
            self.resultado.loc[len(self.resultado)] = [produto, qtd, encontrou]
            self.resultado.to_excel('resultado.xlsx')
        except PermissionError as e:
            print("#"*50)
            print("Permissão para editar o arquivo negada. Feche o arquivo e tente novamente.")
            print(e)

