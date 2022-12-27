"""
Mapeamento da Tela http://lyra:82/financeiro/contapagar

Não adicionar eventos, apenas mapeamento
"""

class ContaPagar:

    def __init__(self, page):
        self.page = page

    @property
    def bntAdicionar(self):
        return self.page.get_by_role("button", name="Adicionar uma linha")

    @property
    def fornecedor(self):
        return self.page.locator("#PessoaId")

    @property
    def documentoFiscal(self):
        return self.page.locator("#DocumentoFiscal")

    @property
    def especie(self):
        return self.page.locator("#Especie")

    @property
    def contaFinanceiraOrigem(self):
        return self.page.locator("#PlanoFinanceiroId")

    @property
    def btnSalvar(self):
        return self.page.get_by_role("button", name=" Salvar")

    @property
    def abaPagamento(self):
        return self.page.get_by_role("link", name="Pagamento")

    @property
    def condicaoPagamento(self):
        return self.page.locator("#CondicaoPagamentoId")

    @property
    def btnExcluirRegistro(self):
        return self.page.locator("td:nth-child(4) > a:nth-child(2)")

    @property
    def bntConfirmarSim(self):
        return self.page.get_by_role("button", name="Sim")
    @property
    def selecaoMotivoCancelamento(self):
        return self.page.locator("#dx_MotivoCancelamentoId").get_by_role("button", name="Select")

    def selecaoLista(self, descricao):
        return self.page.locator("[class='dx-item-content dx-list-item-content']", has_text=descricao)

    def botaoGenerico(self, descricao):
        return self.page.get_by_role("button", name=descricao)

    @property
    def valorTotal(self):
        return self.page.locator("#ValorTotal")
