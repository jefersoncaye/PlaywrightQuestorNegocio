Feature: Example BDD tests

    Scenario: Não deve aparecer Grid durante o Periodo se suspensao
        Given Que Tenha acesso ao Questor Negocio com Usuario e Senha Validos
        When Eu filtre tais dados em Faturamento Agrupado
        Then Deve Aparecer tal resultado