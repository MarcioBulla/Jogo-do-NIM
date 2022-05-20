"""Jogo do NIM contra a maquina invencível,
    Regra:
        - Jogador define número de peças existentes no jogo;
        - Jogador define limite para retirar peças do jogo;
        - Jogador retira peças que seja menor que o limite; e
        - Ganha o o ultimo que retirar peças.
    """

from time import sleep


def input_int(texto):
    """Garantir que o numero inserido seja inteiro diferente de zero

    Args:
        texto (str): texto para pergunta

    Returns:
        int: Numero inteiro diferente de zero
    """
    numero = None
    while not isinstance(numero, int):
        numero = input(texto)
        try:
            numero = float(numero)
            if not numero % 1 == 0:
                print("Erro!!!\nNão digitou um inteiro")
            elif numero == 0:
                print("Erro!!!\nDigite um valor diferente de zero!")
            else:
                return int(numero)
        except ValueError:
            print("Erro!!!\nVocê não digitou um numero valido")


def quem_comeca(pecas, limite):
    """Definir que começa

    Args:
        pecas (int): Número de peças em jogo
        limite (int): Numero limite para retirar peças

    Returns:
        bool: True para jogador começar e False para maquina
    """
    if pecas % (limite+1) == 0:
        print("Você começa!")
        return True
    else:
        print("Maquina começa!")
        return False


def jogada(pecas_em_jogo, limite):
    """Jogada do jogador

    Args:
        pecas_em_jogo (int): Peças em jogo
        limite (int): Limite para retirar peças

    Returns:
        int: quantas peças o jogador irá retirar
    """
    retirar = input_int("Quantas peças ira retirar? ")
    while not retirar <= limite and not retirar <= pecas_em_jogo:
        print(
            f"""Erro!!!
            numero escolhido maior que {limite} e ou {pecas_em_jogo}""")
        retirar = input_int("Quantas peças ira retirar? ")
    return retirar


def maquina(pecas_em_jogo, limite):
    """Jogada da Maquina

    Args:
        pecas_em_jogo (int): Peças em jogo
        limite (int): Limite para retirar peças

    Returns:
        int: quantas peças a maquina retirará
    """
    sleep(.5)
    if pecas_em_jogo <= limite:
        retire = pecas_em_jogo
    elif pecas_em_jogo % (limite+1) != 0:
        retire = 1
        while (pecas_em_jogo - retire) % (limite+1) != 0:
            retire += 1
    else:
        print("Maquina: Você pode vencer!!!")
        retire = 1
    print(f"Maquina retirou {retire} peça(s)")
    return retire


PECAS_EM_JOGO = input_int("Quantas peças em jogo? ")
LIMITE = input_int("Qual o limite para retirar? ")

VEZ = quem_comeca(PECAS_EM_JOGO, LIMITE)
while PECAS_EM_JOGO != 0:
    if VEZ:
        PECAS_EM_JOGO -= jogada(PECAS_EM_JOGO, LIMITE)
        VEZ = False
    else:
        PECAS_EM_JOGO -= maquina(PECAS_EM_JOGO, LIMITE)
        VEZ = True
    sleep(.5)
    print(f"Há {PECAS_EM_JOGO} peças em jogo!!")

if VEZ:
    print("Você Perdeu!!!")
else:
    print("Você ganhou!!!")
