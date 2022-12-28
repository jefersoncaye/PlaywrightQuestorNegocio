"""
Mapeamento da Tela http://lyra:82/Compra/NotaEntrada

Não adicionar eventos, apenas mapeamento
"""

class NotaEntrada:

    def __init__(self, page):
        self.page = page

    @property
    def fornecedor(self):
        return self.page.locator("#PessoaId")

    def selecaoLista(self, descricao):
        return self.page.locator("[class='dx-item-content dx-list-item-content']", has_text=descricao)

    @property
    def sintegraSped(self):
        return self.page.locator("#SintegraSpedId")

    @property
    def especie(self):
        return self.page.locator("#Especie")

    @property
    def serie(self):
        return self.page.locator("#Serie")

    @property
    def documentoFiscal(self):
        return self.page.locator("#DocumentoFiscal")

    @property
    def contaFinanceiraOrigem(self):
        return self.page.locator("#PlanoFinanceiroId")

    @property
    def referente(self):
        return self.page.locator("#Referente")

    @property
    def observacao(self):
        return self.page.locator("#Observacao")

    def bntGenerico(self, nomeBotao):
        return self.page.get_by_role("button", name=nomeBotao)