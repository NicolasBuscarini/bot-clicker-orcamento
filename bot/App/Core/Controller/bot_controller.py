import time

import pygetwindow as pygetwindow

from bot.App.Core.Service.bot_service import BotService
from bot.App.Presentation.usuario_presentation import InterfaceUsuario
from bot.App.Util.json_util import JsonUtil


class BotController:
    def __init__(self, componentes, tempo_entre_acoes: float, caracteres_indesejados: str, filial: str,
                 dic_produtos: JsonUtil, paths: dict):
        self.__bot = BotService(componentes,
                                tempo_entre_acoes,
                                caracteres_indesejados,
                                filial,
                                dic_produtos,
                                paths['planilha_execucao'],
                                paths['planilha_resultado'])

        self.interface_grafica = InterfaceUsuario(path_config=paths['config'],
                                                  path_planilha_execucao=paths['planilha_execucao'],
                                                  path_planilha_resultado=paths['planilha_resultado'])

    def initialize_bot(self):
        try:
            self.interface_grafica.initial()
            BotController.trocar_janela('Protheus')
            self.__bot.execute()
            BotController.trocar_janela('PyWebIO')
            self.interface_grafica.final()
        except Exception as e:
            self.interface_grafica.error(e)
            print("#" * 50)
            print('Erro ao executar o bot. Verifique se o programa está aberto e tente novamente.')
            print(e)

    @staticmethod
    def trocar_janela(janela: str):
        """
        Troca a janela ativa para a janela passada como parâmetro.
        :param janela: Nome da janela que será aberta.
        """
        try:
            pygetwindow.getWindowsWithTitle(janela)[0].activate()
            time.sleep(1)
        except IndexError:
            raise IndexError(f'Não foi possível encontrar a janela do {janela}. Verifique se a janela está aberta.')
