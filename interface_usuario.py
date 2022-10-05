# A simple script to calculate BMI
from pywebio.input import input, FLOAT, NUMBER
from pywebio.output import put_text

def bmi():
    FILIAL = input("Digite a FILIAL：", type=NUMBER)
    ok = input("Deixe a tela de selecionar itens para orçamento em segundo plano", type=NUMBER)

if __name__ == '__main__':
    bmi()