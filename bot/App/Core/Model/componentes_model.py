class ComponentesModel:
    def __init__(self, json):
        self.input_filial: dict = json['inputFilial']
        self.input_descricao: dict = json['inputDescricao']
        self.column_descricao: dict = json['columnDescricao']
