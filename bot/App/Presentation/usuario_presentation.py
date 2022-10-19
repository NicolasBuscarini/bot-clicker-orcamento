import time

from pywebio.input import input as inp, NUMBER, TEXT, file_upload
from pywebio.output import put_text, clear, toast, use_scope, put_file

from App.Util.json_util import JsonUtil


class InterfaceUsuario:

    def __init__(self, *,  path_config, path_planilha_execucao, path_planilha_resultado):
        self.path_config = path_config
        self.path_planilha_execucao = path_planilha_execucao
        self.path_planilha_resultado = path_planilha_resultado

    def initial(self):
        """Initial interface"""
        json = JsonUtil(self.path_config)
        self.ask_filial(json)

        self.ask_file()

        put_text("O bot irá iniciar... Mantenha está janela aberta e não utilize seu teclado nem mouse até que o bot "
                 "termine.")
        put_text("Para interromper o bot mova o mouse para um dos cantos da tela.")
        time.sleep(3)

    @staticmethod
    def ask_filial(json: JsonUtil):
        """Ask filial"""
        with use_scope('scope_filial'):
            filial = inp("Digite a FILIAL：", type=TEXT)
            if filial is None:
                clear("scope_filial")
                toast("Filial incorreto.", position="center", color="error")
                InterfaceUsuario.ask_filial(json)
                return
            json.set('filial', str(filial))
            json.write()

    def ask_file(self):
        """Ask for file"""
        try:
            with use_scope('scope_file'):

                f = file_upload("Upload o arquivo", accept=".xlsx")

                if not f or not f['filename'].endswith(".xlsx"):
                    clear("scope_file")
                    toast("File not found.", position="center", color="error")
                    self.ask_file()
                    return
                file = open(self.path_planilha_execucao, 'wb')
                file.write(f['content'])
                file.close()
                
        except PermissionError as e:
            er = PermissionError("Erro ao enviar arquivo. Favor feche o arquivo e tente novamente.\n" + str(e))
            raise er

    def final(self):
        """
        Tela final para download de planilha resultado
        :return:
        """
        with use_scope('scope_file'):
            put_text("Bot finalizado com sucesso. Agora você pode baixar o arquivo: ")
            try:
                content = open(self.path_planilha_resultado, 'rb').read()
                put_file('Resultado.xlsx', content, 'download')
            except FileNotFoundError:
                er = FileNotFoundError("Erro gerando tabela de resultado. Favor tente novamente.\nNão foi encontrada a "
                                       "planilha para disponibilizar pro download")
                raise er

    @staticmethod
    def error(e: Exception):
        """
           :param e: Exception
           :return: None
        """
        put_text(" ")
        put_text("Erro ao executar o bot. Verifique se o programa está aberto e tente novamente.")
        put_text(e)
