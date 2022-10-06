# A simple script to calculate BMI
from pywebio.input import input as inp, NUMBER, file_upload
from pywebio.output import put_text, clear, toast, use_scope
from Util.json_util import Json


class InterfaceUsuario:

    @staticmethod
    def initial(*, error_message=None):
        """Initial interface"""
        json = Json('Config/config.json')
        InterfaceUsuario.ask_filial(json)

        InterfaceUsuario.ask_file()

        put_text("O bot irá iniciar... Não utilize seu teclado nem mouse até que o bot termine.")
        put_text("Para interromper o bot mova o mouse para um dos cantos da tela.")

    @staticmethod
    def ask_filial(json: Json):
        """Ask filial"""
        with use_scope('scope_filial'):
            filial = inp("Digite a FILIAL：", type=NUMBER)
            if filial is None:
                clear("scope_filial")
                toast("Filial incorreto.", position="center", color="error")
                InterfaceUsuario.ask_filial(json)
                return
            json.set('filial', filial)
            json.write()

    @staticmethod
    def ask_file():
        """Ask for file"""
        with use_scope('scope_file'):
            f = file_upload("Upload a file", accept=".xlsx")

            if not f or not f['filename'].endswith(".xlsx"):
                clear("scope_file")
                toast("File not found.", position="center", color="error")
                InterfaceUsuario.ask_file()
                return
            open('Excel/Execucao.xlsx', 'wb').write(f['content'])

    @staticmethod
    def error(e: Exception):
        """
           :param e: Exception
           :return: None
        """
        put_text("Erro ao executar o bot. Verifique se o programa está aberto e tente novamente.")
        put_text(e)
