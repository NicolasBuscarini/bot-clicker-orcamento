from App.Core.Controller.bot_controller import BotController
from App.Util.json_util import JsonUtil

paths = {'config': 'Config/config.json', 'dicionario': 'Config/dicionario.json',
         'planilha_execucao': 'Assets/IO/Input/Execucao.xlsx', 'planilha_resultado': 'Assets/IO/Output/Resultado.xlsx'}


def main():
    # FAZENDO LEITURA DO DICIONARIO DE PRODUTOS
    dicionario_produtos = JsonUtil(paths['dicionario'])

    # INICIANDO BOT
    controller = BotController(dicionario_produtos, paths)
    controller.initialize_bot()


if __name__ == '__main__':
    main()
