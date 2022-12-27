from PageObjects.Faturamento.faturamentocontratoagrupado import FaturamentoContratoAgrupado
from Utilitarios.acoesPersonalizadas import AcoesPersonalizadas

def filtrosFaturamentoAgrupado(page, dataInicial, dataFinal, numeroContrato = ''):
    ap = AcoesPersonalizadas(page)
    faturamentocontratoagrupado = FaturamentoContratoAgrupado(page)
    ap.navegar("http://lyra:82/faturamento/faturamentocontratoagrupado")
    ap.click(faturamentocontratoagrupado.dataInicial, 'Data Inicial')
    ap.press(faturamentocontratoagrupado.dataInicial, 'Home')
    ap.type(faturamentocontratoagrupado.dataInicial, dataInicial)
    ap.click(faturamentocontratoagrupado.dataFinal, 'Data Final')
    ap.press(faturamentocontratoagrupado.dataFinal, 'Home')
    ap.type(faturamentocontratoagrupado.dataFinal, dataFinal)
    if len(numeroContrato) != 0:
        ap.click(faturamentocontratoagrupado.contrato, 'Contrato')
        ap.type(faturamentocontratoagrupado.contrato, numeroContrato)
        ap.click(faturamentocontratoagrupado.selecaoLista(numeroContrato), numeroContrato)
    ap.click(faturamentocontratoagrupado.tipoOrdenacao, 'Tipo Ordenação')
    ap.click(faturamentocontratoagrupado.selecaoLista('Código'), 'Código')
    ap.click(faturamentocontratoagrupado.formaDeFaturamento, 'Forma de Faturamento')
    ap.click(faturamentocontratoagrupado.selecaoLista('Todas'), 'Todas')
    ap.click(faturamentocontratoagrupado.btnFiltrar, 'Botão Filtrar')