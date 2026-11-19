from idade import MINIMA, idade_permitida


def test_rf01_idade_exatamente_minima_e_aceita():
    # Preparar
    idade = MINIMA
    # Agir
    resultado = idade_permitida(idade)
    # Verificar
    assert resultado is True


def test_rf02_idade_abaixo_da_minima_e_rejeitada():
    # Preparar
    idade = MINIMA - 1
    # Agir
    resultado = idade_permitida(idade)
    # Verificar
    assert resultado is False


def test_rf03_idade_acima_de_cem_e_rejeitada():
    # Preparar
    idade = 101
    # Agir
    resultado = idade_permitida(idade)
    # Verificar
    assert resultado is False
