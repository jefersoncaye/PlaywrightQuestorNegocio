import time

import pytest
import Utilitarios.Login
from PageObjects.Financeiro.contapagar import ContaPagar
from playwright.sync_api import expect

def lancamentoContasPagar(page, fornecedor, documento, especie, condicaoPagemento, valorTotal = ''):
    page.goto("http://lyra:82/financeiro/contapagar")
    contapagar = ContaPagar(page)
    contapagar.bntAdicionar.click()
    time.sleep(1.5)
    contapagar.fornecedor.type(fornecedor)
    time.sleep(1.5)
    contapagar.selecaoLista(fornecedor).click()
    contapagar.documentoFiscal.fill(documento)
    contapagar.especie.fill(especie)
    contapagar.contaFinanceiraOrigem.type("cliente")
    time.sleep(1.5)
    contapagar.selecaoLista("15 - 1.04.01 - Clientes").click()
    contapagar.btnSalvar.click()
    contapagar.abaPagamento.click()
    contapagar.condicaoPagamento.type(condicaoPagemento)
    if valorTotal == '':
        page.wait_for_selector("[class='dx-empty-message']")
        time.sleep(1)
        expect(page.locator("[class='dx-empty-message']")).to_have_text("Sem dados")
    else:
        time.sleep(1)
        contapagar.selecaoLista(condicaoPagemento).click()
        contapagar.valorTotal.fill(valorTotal)
        contapagar.botaoGenerico("Gerar").click()
    page.goto("http://lyra:82/financeiro/contapagar")
    time.sleep(1.5)
    contapagar.btnExcluirRegistro.first.click()
    contapagar.botaoGenerico("Sim").click()
    contapagar.selecaoMotivoCancelamento.click()
    contapagar.selecaoLista("20 - TestComplete motivo cancelamento contas a pagar/receber").click()
    contapagar.botaoGenerico("Confirmar").click()

@pytest.mark.Financeiro
def test_finProcessosLancamentoCPEmpresaAgrupador(set_up):
    page = set_up
    Utilitarios.Login.LoginQN(page, usuario='tc@questores.com.br', senha='123qwe', empresa='1 - Testes Cadastros')
    lancamentoContasPagar(page, fornecedor='Tiririca', documento='123456', especie='boleto',
                          condicaoPagemento='teste agrupamento 30 dias')
    page.close()


