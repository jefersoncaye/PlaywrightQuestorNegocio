class AcoesPersonalizadas:

    def __init__(self, page):
        self.page = page

    def navegar(self, url):
        self.page.on("console", print(f'navegando para a pagina: {url}'))
        self.page.goto(url)

    def click(self, elemento, localClicado):
        self.page.on("console", print(f'clicando em/no {localClicado}'))
        elemento.click()

    def press(self, elemento, tecla):
        self.page.on("console", print(f'pressionando a tecla {tecla}'))
        elemento.press(tecla)

    def type(self, elemento, valor):
        self.page.on("console", print(f'escrevendo {valor}'))
        elemento.type(valor)






