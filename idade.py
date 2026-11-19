MINIMA = 14  # 12 + ultimo digito da matricula (2)


def idade_permitida(idade):
    if idade > 100:
        return False
    return idade >= MINIMA
