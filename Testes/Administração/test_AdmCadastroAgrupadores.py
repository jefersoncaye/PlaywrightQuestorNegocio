import time
import pytest
import Utilitarios.Login
from PageObjects.Administracao.agrupador import Agrupador
from playwright.sync_api import expect

def cadastroAgrupador(page) -> None:
    agrupador = Agrupador(page)
    page.goto("http://lyra:82/administracao/agrupador")
    time.sleep(1)
    agrupador.btnInserir.click()
    agrupador.descricao.fill("teste de agrupador de condição de pagamento")
    agrupador.tipoDeAgrupador.click()
    agrupador.selecaoLista("Condição de Pagamento").click()
    page.get_by_role("treeitem", name="Testes Automatizados").get_by_role("checkbox").click()
    agrupador.btnSalvar.click()

def exclusaoAgrupador(page) -> None:
    agrupador = Agrupador(page)
    page.goto("http://lyra:82/administracao/agrupador")
    time.sleep(1)
    agrupador.pesquisaDescricaoGrid.fill("teste de agrupador de condição de pagamento")
    agrupador.pesquisaDescricaoGrid.press("Enter")
    agrupador.btnApagarNoGrid.first.click()
    page.get_by_role("button", name="Sim").click()
    expect(page.get_by_text("O registro foi removido com sucesso.")).to_have_text("O registro foi removido com sucesso.")
    time.sleep(2)


@pytest.mark.Administracao
def test_AdmCadastroAgrupadores(set_up):
    page = set_up
    Utilitarios.Login.LoginQN(page, usuario='tc@questores.com.br', senha='123qwe', empresa='1 - Testes Cadastros')
    cadastroAgrupador(page)
    exclusaoAgrupador(page)
    page.close()






