from App.Core.Controller.bot_controller import BotController
from App.Util.json_util import JsonUtil

paths = {'config': 'Config/config.json', 'dicionario': 'Config/dicionario.json',
         'planilha_execucao': 'Assets/IO/Input/Execucao.xlsx', 'planilha_resultado': 'Assets/IO/Output/Resultado.xlsx'}


def main():
    # FAZENDO LEITURA DA CONFIGURAÇÃO
    config_json = JsonUtil(paths['config'])

    # FAZENDO LEITURA DO DICIONARIO DE PRODUTOS
    dicionario_produtos = JsonUtil(paths['dicionario'])

    # Pegando dados do config.json
    componentes = config_json.get('componentes')
    tempo_entre_acoes = config_json.get('tempoEntreAcoes')
    caracteres_indesejados = config_json.get('caracteresIndesejados')
    filial = config_json.get('filial')

    # INICIANDO BOT
    controller = BotController(componentes, tempo_entre_acoes, caracteres_indesejados,
                               filial, dicionario_produtos, paths)
    controller.initialize_bot()


if __name__ == '__main__':
    main()
