# A simple script to calculate BMI
from pywebio.input import input as inp, NUMBER, file_upload
from pywebio.output import put_text
from Util.json_util import Json


class InterfaceUsuario:

    @staticmethod
    def initial():
        """Initial interface"""
        json = Json('Config/config.json')
        filial = inp("Digite a FILIAL：", type=NUMBER)
        json.set('filial', filial)
        json.write()

        f = file_upload("Upload a file")
        open('asset/' + f['filename'], 'wb').write(f['content'])

        put_text("O bot irá iniciar... Não utilize seu teclado nem mouse até que o bot termine.")
        put_text("Para interromper o bot mova o mouse para um dos cantos da tela.")

    @staticmethod
    def error(e: Exception):
        """
           :param e: Exception
           :return: None
        """
        put_text("Erro ao executar o bot. Verifique se o programa está aberto e tente novamente.")
        put_text(e)
