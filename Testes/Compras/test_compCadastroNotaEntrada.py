import pytest
import Utilitarios.Login
from PageObjects.Compra.notaentrada import NotaEntrada
from Utilitarios.acoesPersonalizadas import AcoesPersonalizadas

def cobecalhoNotaEntrada(page, fornecedor, sintegraSped, especie, serie, documento, contaFinanceiraOrigem,
                         referente = '', observacao = ''):
    notaEntrada = NotaEntrada(page)
    ap = AcoesPersonalizadas(page)
    ap.navegar("http://lyra:82/Compra/NotaEntrada/Inserir?masterId=")
    ap.click(notaEntrada.fornecedor, 'Fornecedor')
    ap.fill(notaEntrada.fornecedor, fornecedor)
    ap.click(
        notaEntrada.selecaoLista(fornecedor), fornecedor)
    ap.click(notaEntrada.sintegraSped, 'Sintegra/Sped')
    ap.fill(notaEntrada.sintegraSped, sintegraSped)
    ap.click(notaEntrada.selecaoLista(sintegraSped), sintegraSped)
    ap.click(notaEntrada.especie, 'Especie')
    ap.fill(notaEntrada.especie, especie)
    ap.click(notaEntrada.serie, 'Série')
    ap.fill(notaEntrada.serie, serie)
    ap.click(notaEntrada.documentoFiscal, 'Documento Fiscal')
    ap.fill(notaEntrada.documentoFiscal, documento)
    ap.click(notaEntrada.contaFinanceiraOrigem, 'Conta Financeira Origem')
    ap.fill(notaEntrada.contaFinanceiraOrigem, contaFinanceiraOrigem)
    ap.click(notaEntrada.selecaoLista(contaFinanceiraOrigem), contaFinanceiraOrigem)
    ap.click(notaEntrada.referente, 'Referente')
    ap.fill(notaEntrada.referente, referente)
    ap.click(notaEntrada.observacao, 'Observação')
    ap.fill(notaEntrada.observacao, observacao)
    ap.click(notaEntrada.bntGenerico(" Salvar"), 'Botão Salvar')


def test_compCadastroNotaEntrada(set_up):
    page = set_up
    Utilitarios.Login.LoginQN(page, usuario='tc@questores.com.br', senha='123qwe', empresa='1 - Testes Cadastros')
    cobecalhoNotaEntrada(page, fornecedor='22 - 41.845.394/0001-66 - Não excluir! Cadastro utilizado em cadastro de nota de',
                         sintegraSped='01 - Nota Fiscal (NF)', especie='NF', serie='1', documento='123456',
                         contaFinanceiraOrigem='36 - 2.02.01 - Fornecedores', referente='testComplete',
                         observacao='testComplete' )
