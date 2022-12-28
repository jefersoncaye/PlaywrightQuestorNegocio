from playwright.sync_api import expect
from PageObjects.Faturamento.faturamentocontratoagrupado import FaturamentoContratoAgrupado
from Utilitarios.acoesPersonalizadas import AcoesPersonalizadas


def validacaoServicosFiltroFaturamentoAgrupado01(page):
    ap = AcoesPersonalizadas(page)
    faturamentocontratoagrupado = FaturamentoContratoAgrupado(page)
    ap.click(faturamentocontratoagrupado.btnAbrirPrimeiroDetalhamentoGridPrincipal.first, 'Detalhamento Grid Empresa 01')
    valorEsperado = 'Recorrente24 - Serv. Recorrente01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente26 - Serv. Desconto01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente27 - Serv. Cancelado01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente28 - Serv. Suspensao01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Variável23 - Serv. Valor Zerado01/02/2021 1R$ 1.000,00R$ 1.000,00'

    ap.expectHaveText(faturamentocontratoagrupado.detalhamentoGripPrincialContratos.last, valorEsperado,
                      'Detalhamento Grid Empresa 01')

def validacaoServicosFiltroFaturamentoAgrupado128(page):
    faturamentocontratoagrupado = FaturamentoContratoAgrupado(page)
    ap = AcoesPersonalizadas(page)
    ap.click(faturamentocontratoagrupado.btnAbrirPrimeiroDetalhamentoGridPrincipal.first, 'Detalhamento Grid Empresa 128')
    valorEsperado = 'Recorrente24 - Serv. Recorrente01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente26 - Serv. Desconto01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente27 - Serv. Cancelado01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente28 - Serv. Suspensao01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Variável23 - Serv. Valor Zerado01/02/2021 1R$ 1.000,00R$ 1.000,00'

    ap.expectHaveText(faturamentocontratoagrupado.detalhamentoGripPrincialContratos.last, valorEsperado,
                      'Detalhamento Grid Empresa 128')

def validacaoServicosFiltroFaturamentoAgrupado129(page):
    faturamentocontratoagrupado = FaturamentoContratoAgrupado(page)
    ap = AcoesPersonalizadas(page)
    ap.click(faturamentocontratoagrupado.btnAbrirPrimeiroDetalhamentoGridPrincipal.first, 'Detalhamento Grid Empresa 129')
    page.on("Console", print("Valida Detalhamento do Grid Principal"))
    valorEsperado = 'Recorrente24 - Serv. Recorrente01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente26 - Serv. Desconto01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente27 - Serv. Cancelado01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente28 - Serv. Suspensao01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Variável23 - Serv. Valor Zerado01/02/2021 1R$ 1.000,00R$ 1.000,00'

    ap.expectHaveText(faturamentocontratoagrupado.detalhamentoGripPrincialContratos.last, valorEsperado,
                      'Detalhamento Grid Empresa 129')

def validacaoServicosFiltroFaturamentoAgrupado130(page):
    faturamentocontratoagrupado = FaturamentoContratoAgrupado(page)
    ap = AcoesPersonalizadas(page)
    ap.click(faturamentocontratoagrupado.btnAbrirPrimeiroDetalhamentoGridPrincipal.first, 'Detalhamento Grid Empresa 130')
    valorEsperado = 'Recorrente24 - Serv. Recorrente01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente26 - Serv. Desconto01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente27 - Serv. Cancelado01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente28 - Serv. Suspensao01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Variável23 - Serv. Valor Zerado01/02/2021 1R$ 1.000,00R$ 1.000,00'

    ap.expectHaveText(faturamentocontratoagrupado.detalhamentoGripPrincialContratos.last, valorEsperado,
                      'Detalhamento Grid Empresa 130')

def validacaoServicosFiltroFaturamentoAgrupado131(page):
    faturamentocontratoagrupado = FaturamentoContratoAgrupado(page)
    ap = AcoesPersonalizadas(page)
    ap.click(faturamentocontratoagrupado.btnAbrirPrimeiroDetalhamentoGridPrincipal.first, 'Detalhamento Grid Empresa 131')
    valorEsperado = 'Recorrente24 - Serv. Recorrente01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente26 - Serv. Desconto01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente27 - Serv. Cancelado01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente28 - Serv. Suspensao01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Variável23 - Serv. Valor Zerado01/02/2021 1R$ 1.000,00R$ 1.000,00'

    ap.expectHaveText(faturamentocontratoagrupado.detalhamentoGripPrincialContratos.last, valorEsperado,
                      'Detalhamento Grid Empresa 131')

def validacaoServicosFiltroFaturamentoAgrupado132(page):
    faturamentocontratoagrupado = FaturamentoContratoAgrupado(page)
    ap = AcoesPersonalizadas(page)
    ap.click(faturamentocontratoagrupado.btnAbrirPrimeiroDetalhamentoGridPrincipal.first, 'Detalhamento Grid Empresa 132')
    valorEsperado = 'Recorrente24 - Serv. Recorrente01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente26 - Serv. Desconto01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente27 - Serv. Cancelado01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente28 - Serv. Suspensao01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Variável23 - Serv. Valor Zerado01/02/2021 1R$ 1.000,00R$ 1.000,00'

    ap.expectHaveText(faturamentocontratoagrupado.detalhamentoGripPrincialContratos.last, valorEsperado,
                      'Detalhamento Grid Empresa 132')

def validacaoServicosFiltroFaturamentoAgrupado133(page):
    faturamentocontratoagrupado = FaturamentoContratoAgrupado(page)
    ap = AcoesPersonalizadas(page)
    ap.click(faturamentocontratoagrupado.btnAbrirPrimeiroDetalhamentoGridPrincipal.first, 'Detalhamento Grid Empresa 133')
    valorEsperado = 'Recorrente24 - Serv. Recorrente01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente26 - Serv. Desconto01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente27 - Serv. Cancelado01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente28 - Serv. Suspensao01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Variável23 - Serv. Valor Zerado01/02/2021 1R$ 1.000,00R$ 1.000,00'

    ap.expectHaveText(faturamentocontratoagrupado.detalhamentoGripPrincialContratos.last, valorEsperado,
                      'Detalhamento Grid Empresa 133')

def validacaoServicosFiltroFaturamentoAgrupado134(page):
    faturamentocontratoagrupado = FaturamentoContratoAgrupado(page)
    ap = AcoesPersonalizadas(page)
    ap.click(faturamentocontratoagrupado.btnAbrirPrimeiroDetalhamentoGridPrincipal.first, 'Detalhamento Grid Empresa 134')
    valorEsperado = 'Recorrente24 - Serv. Recorrente01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente26 - Serv. Desconto01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                   'Recorrente27 - Serv. Cancelado01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                   'Recorrente28 - Serv. Suspensao01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                   'Variável23 - Serv. Valor Zerado01/02/2021 1R$ 1.000,00R$ 1.000,00'

    ap.expectHaveText(faturamentocontratoagrupado.detalhamentoGripPrincialContratos.last, valorEsperado,
                      'Detalhamento Grid Empresa 134')

def validacaoServicosFiltroFaturamentoAgrupado135(page):
    faturamentocontratoagrupado = FaturamentoContratoAgrupado(page)
    ap = AcoesPersonalizadas(page)
    ap.click(faturamentocontratoagrupado.btnAbrirPrimeiroDetalhamentoGridPrincipal.first, 'Detalhamento Grid Empresa 135')
    valorEsperado = 'Recorrente24 - Serv. Recorrente01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente26 - Serv. Desconto01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente27 - Serv. Cancelado01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente28 - Serv. Suspensao01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Variável23 - Serv. Valor Zerado01/02/2021 1R$ 1.000,00R$ 1.000,00'

    ap.expectHaveText(faturamentocontratoagrupado.detalhamentoGripPrincialContratos.last, valorEsperado,
                      'Detalhamento Grid Empresa 135')

def validacaoServicosFiltroFaturamentoAgrupado136(page):
    faturamentocontratoagrupado = FaturamentoContratoAgrupado(page)
    ap = AcoesPersonalizadas(page)
    ap.click(faturamentocontratoagrupado.btnAbrirPrimeiroDetalhamentoGridPrincipal.first, 'Detalhamento Grid Empresa 136')
    valorEsperado = 'Recorrente24 - Serv. Recorrente01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente26 - Serv. Desconto01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente27 - Serv. Cancelado01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Recorrente28 - Serv. Suspensao01/02/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                    'Variável23 - Serv. Valor Zerado01/02/2021 1R$ 1.000,00R$ 1.000,00'

    ap.expectHaveText(faturamentocontratoagrupado.detalhamentoGripPrincialContratos.last, valorEsperado,
                      'Detalhamento Grid Empresa 136')