
import pytest
import Utilitarios.Login
from Testes.Financeiro.test_finProcessosLancamentoCPEmpresaAgrupador import lancamentoContasPagar


@pytest.mark.Financeiro
def test_finProcessosLancamentoCPEmpresaNaoAgrupador(set_up):
    page = set_up
    Utilitarios.Login.LoginQN(page, usuario='tc@questores.com.br', senha='123qwe', empresa='1 - Testes Cadastros')
    lancamentoContasPagar(page, fornecedor='Tiririca', documento='123456', especie='boleto',
                          condicaoPagemento='2 x Boleto', valorTotal= '150')
    page.close()
