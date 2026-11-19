MINIMA = 14  # 12 + ultimo digito da matricula (2)


def idade_permitida(idade):
    if type(idade) is not int:
        return False
    if idade > 100:
        return False
    return idade >= MINIMA
