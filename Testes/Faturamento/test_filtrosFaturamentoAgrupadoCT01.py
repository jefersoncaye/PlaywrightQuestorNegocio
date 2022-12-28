import pytest
import Utilitarios.Login
from PageObjects.Faturamento.faturamentocontratoagrupado import FaturamentoContratoAgrupado
from Utilitarios.FaturamentoAgrupado import validaFiltrosFaturamentoAgrupado, filtrosFaturamentoAgrupado
from Utilitarios.acoesPersonalizadas import AcoesPersonalizadas



def validacaoFiltroFaturamentoAgrupadoContratos01a136(page):
    ap = AcoesPersonalizadas(page)
    faturamentocontratoagrupado = FaturamentoContratoAgrupado(page)
    valorEsperado = '98 - EMPRESA USADA EM TESTE AUTOMATIZADO DE CONTRATO TRF: #2051010Contrato 1Não InformadoCond. Pgto 1 - Testes Katia Filtros Faturamento  ' \
                    '225 - EMPRESA USADA EM TESTE AUTOMATIZADO DE CONTRATO TRF: #2051010128Não InformadoCond. Pgto 1 - Testes Katia Filtros Faturamento  ' \
                    '226 - EMPRESA USADA EM TESTE AUTOMATIZADO DE CONTRATO TRF: #2051010129Não InformadoCond. Pgto 1 - Testes Katia Filtros Faturamento  ' \
                    '227 - EMPRESA USADA EM TESTE AUTOMATIZADO DE CONTRATO TRF: #2051010130Não InformadoCond. Pgto 1 - Testes Katia Filtros Faturamento  ' \
                    '228 - EMPRESA USADA EM TESTE AUTOMATIZADO DE CONTRATO TRF: #2051010131Não InformadoCond. Pgto 1 - Testes Katia Filtros Faturamento  ' \
                    '229 - EMPRESA USADA EM TESTE AUTOMATIZADO DE CONTRATO TRF: #2051010132Não InformadoCond. Pgto 2 - Testes Katia Filtros Faturamento  ' \
                    '230 - EMPRESA USADA EM TESTE AUTOMATIZADO DE CONTRATO TRF: #2051010133Não InformadoCond. Pgto 2 - Testes Katia Filtros Faturamento  ' \
                    '231 - EMPRESA USADA EM TESTE AUTOMATIZADO DE CONTRATO TRF: #2051010134Não InformadoCond. Pgto 2 - Testes Katia Filtros Faturamento  ' \
                    '232 - EMPRESA USADA EM TESTE AUTOMATIZADO DE CONTRATO TRF: #2051010135Não InformadoCond. Pgto 2 - Testes Katia Filtros Faturamento  ' \
                    '233 - EMPRESA USADA EM TESTE AUTOMATIZADO DE CONTRATO TRF: #2051010136Não InformadoCond. Pgto 2 - Testes Katia Filtros Faturamento'
    ap.expectHaveText(faturamentocontratoagrupado.gripPrincialContratos, valorEsperado, 'Grid Principal')

@pytest.mark.Faturamento
@pytest.mark.FaturamentoAgrupado
def test_filtrosFaturamentoAgrupadoCT01(set_up):
    page = set_up
    Utilitarios.Login.LoginQN(page, usuario='lupitapuente@gmail.com.br', senha='abc*123', empresa='4 - Testes Faturamento Katia')
    filtrosFaturamentoAgrupado.filtrosFaturamentoAgrupado(page, dataInicial='01022021', dataFinal='28022021')
    validacaoFiltroFaturamentoAgrupadoContratos01a136(page)
    validaFiltrosFaturamentoAgrupado.validacaoServicosFiltroFaturamentoAgrupado01(page)
    validaFiltrosFaturamentoAgrupado.validacaoServicosFiltroFaturamentoAgrupado128(page)
    validaFiltrosFaturamentoAgrupado.validacaoServicosFiltroFaturamentoAgrupado129(page)
    validaFiltrosFaturamentoAgrupado.validacaoServicosFiltroFaturamentoAgrupado130(page)
    validaFiltrosFaturamentoAgrupado.validacaoServicosFiltroFaturamentoAgrupado131(page)
    validaFiltrosFaturamentoAgrupado.validacaoServicosFiltroFaturamentoAgrupado132(page)
    validaFiltrosFaturamentoAgrupado.validacaoServicosFiltroFaturamentoAgrupado133(page)
    validaFiltrosFaturamentoAgrupado.validacaoServicosFiltroFaturamentoAgrupado134(page)
    validaFiltrosFaturamentoAgrupado.validacaoServicosFiltroFaturamentoAgrupado135(page)
    validaFiltrosFaturamentoAgrupado.validacaoServicosFiltroFaturamentoAgrupado136(page)
    page.on("Console", print("Fim do teste"))
    page.close()