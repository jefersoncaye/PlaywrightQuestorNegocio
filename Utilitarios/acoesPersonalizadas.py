from playwright.sync_api import expect

class AcoesPersonalizadas:

    def __init__(self, page):
        self.page = page

    def navegar(self, url):
        self.page.on("console", print(f'navegando para a pagina: {url}'))
        self.page.goto(url)

    def click(self, elemento, localClicado = ''):
        if localClicado == '':
            localClicado = elemento
        self.page.on("console", print(f'clicando em/no: {localClicado}'))
        elemento.click()

    def press(self, elemento, tecla):
        self.page.on("console", print(f'pressionando a tecla: {tecla}'))
        elemento.press(tecla)

    def type(self, elemento, valor):
        self.page.on("console", print(f'escrevendo: {valor}'))
        elemento.type(valor)

    def fill(self, elemento, valor):
        self.page.on("console", print(f'colando texto: {valor}'))
        elemento.fill(valor)

    def expectHaveText(self, elemento, valorEsperado, nomeObjetoAValidar = ''):
        if nomeObjetoAValidar == '':
            nomeObjetoAValidar = elemento
        self.page.on("console", print(f'Validando se o elemento: {nomeObjetoAValidar} possui o texto: \n{valorEsperado}\n'))
        expect(elemento).to_have_text(valorEsperado)



