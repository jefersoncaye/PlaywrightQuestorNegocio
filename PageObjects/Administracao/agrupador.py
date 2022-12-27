
"""
Mapeamento da Tela http://lyra:82/administracao/agrupador

Não adicionar eventos, apenas mapeamento
"""

class Agrupador:

    def __init__(self, page):
        self.page = page

    @property
    def btnInserir(self):
        return self.page.get_by_role("button", name="Inserir")

    @property
    def descricao(self):
        return self.page.locator("#Descricao")

    @property
    def tipoDeAgrupador(self):
        return self.page.locator("#TipoAgrupador")

    def selecaoLista(self, descricao):
        return self.page.locator("[class='dx-item-content dx-list-item-content']", has_text=descricao)

    @property
    def btnSalvar(self):
        return self.page.locator('xpath=//*[@id="save"]')

    @property
    def pesquisaDescricaoGrid(self):
        return self.page.get_by_role("textbox")

    @property
    def btnApagarNoGrid(self):
        return self.page.get_by_role("link", name="Eliminar")