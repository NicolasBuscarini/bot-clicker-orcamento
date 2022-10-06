from bot.App.Service.botorcamento_service import BotOrcamento
from bot.App.Util.json_util import JsonUtil
from bot.App.InterfaceGrafica.usuario_interfacegrafica import InterfaceUsuario

PATH_CONFIG = 'Config/config.json'
PATH_DICIONARIO = 'Config/dicionario.json'
PATH_PLANILHA_EXECUCAO = 'Excel/Execucao.xlsx'
PATH_PLANILHA_RESULTADO = 'Excel/Resultado.xlsx'


def main():
    # FAZENDO LEITURA DA CONFIGURAÇÃO
    config_json = JsonUtil(PATH_CONFIG)

    # FAZENDO LEITURA DO DICIONARIO DE PRODUTOS
    dicionario_produtos = JsonUtil(PATH_DICIONARIO)

    # Pegando dados do config.json
    componentes = config_json.get('componentes')
    tempo_entre_acoes = config_json.get('tempoEntreAcoes')
    caracteres_indesejados = config_json.get('caracteresIndesejados')
    filial = config_json.get('filial')

    interface_grafica = InterfaceUsuario(path_config=PATH_CONFIG, path_planilha_execucao=PATH_PLANILHA_EXECUCAO,
                                         path_planilha_resultado=PATH_PLANILHA_RESULTADO)
    interface_grafica.initial()

    # INICIANDO BOT
    try:
        bot = BotOrcamento(componentes, tempo_entre_acoes, caracteres_indesejados, filial, dicionario_produtos,
                           PATH_PLANILHA_EXECUCAO, PATH_PLANILHA_RESULTADO)
        bot.initialize()
        interface_grafica.final()
    except Exception as e:
        interface_grafica.error(e)
        print("#" * 50)
        print('Erro ao executar o bot. Verifique se o programa está aberto e tente novamente.')
        print(e)


if __name__ == '__main__':
    main()
