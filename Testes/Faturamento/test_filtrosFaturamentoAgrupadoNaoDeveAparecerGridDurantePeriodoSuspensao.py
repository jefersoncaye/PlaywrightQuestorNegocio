import pytest
import Utilitarios.Login
from PageObjects.Faturamento.faturamentocontratoagrupado import FaturamentoContratoAgrupado
from Utilitarios.FaturamentoAgrupado import filtrosFaturamentoAgrupado
from playwright.sync_api import expect
from Utilitarios.acoesPersonalizadas import AcoesPersonalizadas


def validacaoServicosContrato(page, casoTeste):
    ap = AcoesPersonalizadas(page)
    faturamentocontratoagrupado = FaturamentoContratoAgrupado(page)
    ap.expectHaveText(faturamentocontratoagrupado.gripPrincialContratos.last, '103 - AES TIETE ENERGIA SAcontrato seisNão Informado',
                      'Grid Principal')
    ap.click(faturamentocontratoagrupado.btnAbrirPrimeiroDetalhamentoGridPrincipal.first, 'Primeiro Detalhamento do Grid Principal não Aberto')
    if casoTeste == 1:
        valorEsperado1 = 'Recorrente24 - Serv. Recorrente01/12/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                         'Recorrente26 - Serv. Desconto01/12/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                         'Recorrente27 - Serv. Cancelado01/12/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                         'Recorrente28 - Serv. Suspensao01/12/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                         'Variável23 - Serv. Valor Zerado01/12/2021 1R$ 1.000,00R$ 1.000,00'
        ap.expectHaveText(faturamentocontratoagrupado.detalhamentoGripPrincialContratos.last, valorEsperado1,
                          'Detalhamento Grid Principal Caso 1')
    if casoTeste == 2:
        valorEsperado2 = 'Recorrente24 - Serv. Recorrente01/12/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                         'Recorrente26 - Serv. Desconto01/12/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                         'Recorrente27 - Serv. Cancelado01/12/2021Indeterminado1R$ 1.000,00R$ 1.000,00'
        ap.expectHaveText(faturamentocontratoagrupado.detalhamentoGripPrincialContratos.last, valorEsperado2,
                          'Detalhamento Grid Principal Caso 2')
    if casoTeste == 3:
        valorEsperado3 = 'Recorrente24 - Serv. Recorrente01/12/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                         'Recorrente26 - Serv. Desconto01/12/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                         'Recorrente27 - Serv. Cancelado01/12/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                         'Recorrente28 - Serv. Suspensao01/12/2021Indeterminado1R$ 1.000,00R$ 1.000,00'
        ap.expectHaveText(faturamentocontratoagrupado.detalhamentoGripPrincialContratos.last, valorEsperado3,
                          'Detalhamento Grid Principal Caso 3')
    if casoTeste == 4:
        valorEsperado4 = 'Recorrente24 - Serv. Recorrente01/12/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                         'Recorrente26 - Serv. Desconto01/12/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                         'Recorrente27 - Serv. Cancelado01/12/2021Indeterminado1R$ 1.000,00R$ 1.000,00' \
                         'Recorrente28 - Serv. Suspensao01/12/2021Indeterminado1R$ 1.000,00R$ 1.000,00'
        ap.expectHaveText(faturamentocontratoagrupado.detalhamentoGripPrincialContratos.last, valorEsperado4,
                          'Detalhamento Grid Principal Caso 4')

@pytest.mark.Faturamento
@pytest.mark.FaturamentoAgrupado
def test_filtrosFaturamentoAgrupadoNaoDeveAparecerGridDurantePeriodoSuspensao(set_up):
    page = set_up
    Utilitarios.Login.LoginQN(page, usuario='azahararnau@gmail.com.br', senha='abc*123',
                              empresa='4 - Testes Faturamento Katia')
    filtrosFaturamentoAgrupado.filtrosFaturamentoAgrupado(page, dataInicial='01122021',
                              dataFinal='31122021', numeroContrato='contrato seis')
    validacaoServicosContrato(page, casoTeste=1)
    filtrosFaturamentoAgrupado.filtrosFaturamentoAgrupado(page, dataInicial='10122021',
                              dataFinal='20122021', numeroContrato='contrato seis')
    validacaoServicosContrato(page, casoTeste=2)
    filtrosFaturamentoAgrupado.filtrosFaturamentoAgrupado(page, dataInicial='09122021',
                              dataFinal='20122021', numeroContrato='contrato seis')
    validacaoServicosContrato(page, casoTeste=3)
    filtrosFaturamentoAgrupado.filtrosFaturamentoAgrupado(page, dataInicial='10122021',
                              dataFinal='21122021', numeroContrato='contrato seis')
    validacaoServicosContrato(page, casoTeste=4)
    page.on("Console", print("Fim do Teste"))
    page.close()