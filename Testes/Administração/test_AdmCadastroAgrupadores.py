import time
import pytest
import Utilitarios.Login
from PageObjects.Administracao.agrupador import Agrupador
from Utilitarios.acoesPersonalizadas import AcoesPersonalizadas

def cadastroAgrupador(page) -> None:
    ap = AcoesPersonalizadas(page)
    agrupador = Agrupador(page)
    ap.navegar("http://lyra:82/administracao/agrupador")
    time.sleep(1)
    ap.click(agrupador.btnGenerico("Inserir"), 'Botão Inserir')
    ap.fill(agrupador.descricao, "teste de agrupador de condição de pagamento")
    ap.click(agrupador.tipoDeAgrupador, 'Tipo de Agrupador')
    ap.click(agrupador.selecaoLista("Condição de Pagamento"), 'Condição de Pagamento')
    ap.click(page.get_by_role("treeitem", name="Testes Automatizados").get_by_role("checkbox"), 'CheckBox Testes Automatizados')
    ap.click(agrupador.btnSalvar, 'Botão Salvar')

def exclusaoAgrupador(page) -> None:
    ap = AcoesPersonalizadas(page)
    agrupador = Agrupador(page)
    ap.navegar("http://lyra:82/administracao/agrupador")
    time.sleep(1)
    ap.fill(agrupador.pesquisaDescricaoGrid, "teste de agrupador de condição de pagamento")
    ap.press(agrupador.pesquisaDescricaoGrid, "Enter")
    ap.click(agrupador.linkGenerico("Eliminar").first, 'Primeiro botão de Apagar no Grid')
    ap.click(agrupador.btnGenerico("Sim"), "Sim")
    ap.expectHaveText(page.get_by_text("O registro foi removido com sucesso."), "O registro foi removido com sucesso.",
                      'Mensagem Registro Removido')
    time.sleep(2)


@pytest.mark.Administracao
def test_AdmCadastroAgrupadores(set_up):
    page = set_up
    Utilitarios.Login.LoginQN(page, usuario='tc@questores.com.br', senha='123qwe', empresa='1 - Testes Cadastros')
    cadastroAgrupador(page)
    exclusaoAgrupador(page)
    page.close()






