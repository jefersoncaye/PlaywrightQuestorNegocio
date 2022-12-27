"""
Mapeamento da Tela http://lyra:82/faturamento/faturamentocontratoagrupado

Não adicionar eventos, apenas mapeamento
"""

class FaturamentoContratoAgrupado:

    def __init__(self, page):
        self.page = page

    @property
    def dataInicial(self):
        return self.page.locator("#DataVigenciaInicial")

    @property
    def dataFinal(self):
        return self.page.locator("#DataVigenciaFinal")

    @property
    def tipoOrdenacao(self):
        return self.page.locator("#TipoOrdenacaoEnum")

    def selecaoLista(self, descricao):
        return self.page.locator("[class='dx-item-content dx-list-item-content']", has_text=descricao)

    @property
    def formaDeFaturamento(self):
        return self.page.locator("#FormaFaturamento")

    @property
    def btnFiltrar(self):
        return self.page.get_by_role("button", name=" Filtrar")

    @property
    def gripPrincialContratos(self):
        return self.page.locator('xpath=//*[@id="GridFaturamentoContratoAgrupado"]/div/div[6]/div[1]/div/div[1]/div/table')

    @property
    def detalhamentoGripPrincialContratos(self):
        return self.page.locator(
            'xpath=//*[@id="detailGrid"]/div/div[6]/div/div/div[1]/div/table')

    @property
    def btnAbrirPrimeiroDetalhamentoGridPrincipal(self):
        return self.page.locator(".dx-datagrid-group-closed")

    @property
    def contrato(self):
        return self.page.locator("#ContratoId")
