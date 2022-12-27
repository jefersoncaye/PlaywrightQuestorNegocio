import time

def LoginQN(page, usuario, senha, empresa):
    page.on("console", print(f'Fazendo Login com a empresa: {empresa}, usuario: {usuario}, senha: {senha}'))
    page.goto("http://lyra:82/acesso/entrar", timeout=90000)
    while page.is_visible('xpath=//*[@id="cookieConsent"]',timeout = 2000):
        page.get_by_role("button", name="Permitir").click()
    page.get_by_placeholder("Usuário").fill(usuario)
    page.get_by_placeholder("Senha").fill(senha)
    time.sleep(2)
    page.get_by_role("button", name="ENTRAR").click()
    page.get_by_role("button", name="Select").click()
    page.get_by_text(empresa).click()
    time.sleep(2)
    page.get_by_role("button", name="SELECIONAR").click()
    time.sleep(2)
    page.on("console", print("Login Feito com Sucesso!"))
