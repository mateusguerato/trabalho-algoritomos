# Mateus Machado Guerato ra150436

import sys
from dataclasses import dataclass
from enum import Enum, auto

@dataclass
class Depoimento:
    emissor: str
    destinatario: str
    mensagem: str

@dataclass
class Usuario:
    nome: str 
    aura: int
    amigos: list[str]
    depoimentos: list[Depoimento]

class Aura(Enum):
    FAZER_DEPOIMENTO = auto()
    RECEBER_DEPOIMENTO = auto()
    FAZER_AMIZADE = auto()
    DESFAZER_AMIZADE = auto()
    



def le_arquivo(nome: str) -> list[list[str]]:
    """
    Lê o conteúdo do arquivo *nome* e devolve uma lista onde cada elemento é a lista de apelidos de uma linha (o primeiro é o da pessoa e os demais são os de seus amigos). Por exemplo, se o conteúdo do arquivo for
    Malbarbo Josiane Mauro Flavio
    Josiane Malbarbo
    a resposta produzida é 
    [['Malbarbo', 'Josiane', 'Mauro', 'Flavio'], ['Josiane','Malbarbo']]
    """
    try:
        with open(nome) as f:
            return [linha.split() for linha in f]
    except IOError as e:
        print(f'Erro na leitura do arquivo "{nome}": {e.errno} - {e.strerror}.');
        sys.exit(1)



def existe_usuario(usuario: str, banco_de_dados: list[Usuario]) -> bool:
    """
    confere se o *usuario* existe no *banco_de_dados*

    exemplos:
    >>> banco = [
    ...     Usuario(nome='Mateus', aura=0, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Pedro', aura=0, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Lucas', aura=0, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Yasmin', aura=0, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Diogo', aura=0, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Gabi', aura=0, amigos=[], depoimentos=[]),
    ... ]
    >>> existe_usuario('Mateus', banco)
    True
    >>> existe_usuario('Neymar', banco)
    False
    """
    usuario_ja_existe = False
    i = 0
    while i < len(banco_de_dados) and not usuario_ja_existe:    
        if banco_de_dados[i].nome == usuario:
            usuario_ja_existe = True
        i = i + 1

    return usuario_ja_existe




def importa_amizades(usuario: str, arquivo: list[list[str]]) -> list[str]:
    """
    importa as amizades de determinado *usuario* de um *arquivo*

    exemplos:
    >>> banco = [
    ...     ['Mateus', 'Diogo', 'Pedro', 'Lucas'],
    ...     ['Pedro', 'Mateus', 'Diogo'],
    ...     ['Lucas', 'Mateus', 'Diogo', 'Gabi'],
    ...     ['Yasmin', 'Gabi', 'Diogo'],
    ...     ['Diogo', 'Lucas', 'Mateus', 'Pedro', 'Yasmin'],
    ...     ['Gabi', 'Yasmin', 'Lucas'],
    ... ]

    >>> importa_amizades('Mateus', banco)
    ['Pedro', 'Lucas', 'Diogo']
    >>> importa_amizades('Gabi', banco)
    ['Yasmin', 'Lucas']
    """
    amigos = []
    for i in range(len(arquivo)):
        for j in range(1, len(arquivo[i])):
            if arquivo[i][j] == usuario:
                amigos.append(arquivo[i][0])
    return amigos




def cria_lista_de_usuarios(arquivo: list[list[str]]) -> list[Usuario]:
    """
    cria o usuario para todos as pessoas do *arquivo* sem seus amigos

    fazer funcao que cria o usuario para cada um de todas as listas, nao criando para quem ja tem primeiro, e depois a que reconhece e cria as amizades de cada um

    exemplo
    >>> banco = [
    ...     ['Mateus', 'Diogo', 'Pedro', 'Lucas'],
    ...     ['Pedro', 'Mateus', 'Diogo'],
    ...     ['Lucas', 'Mateus', 'Diogo', 'Gabi'],
    ...     ['Yasmin', 'Gabi', 'Diogo'],
    ...     ['Diogo', 'Lucas', 'Mateus', 'Pedro', 'Yasmin'],
    ...     ['Gabi', 'Yasmin', 'Lucas'],
    ... ]

    >>> cria_lista_de_usuarios(banco)
    [Usuario(nome='Mateus', aura=0, amigos=[], depoimentos=[]), Usuario(nome='Diogo', aura=0, amigos=[], depoimentos=[]), Usuario(nome='Pedro', aura=0, amigos=[], depoimentos=[]), Usuario(nome='Lucas', aura=0, amigos=[], depoimentos=[]), Usuario(nome='Gabi', aura=0, amigos=[], depoimentos=[]), Usuario(nome='Yasmin', aura=0, amigos=[], depoimentos=[])]
    """
    usuarios = []

    for i in range(len(arquivo)):
        for j in range(len(arquivo[i])):
            nome = arquivo[i][j]
            amigos = importa_amizades(arquivo[i][j], arquivo)
            aura = len(amigos) * 100
            depoimentos = []
            usuario_ja_cadastrado = existe_usuario(nome, usuarios)

            if not usuario_ja_cadastrado:
                usuarios.append(Usuario(nome, aura, amigos, depoimentos))

    return usuarios




def cria_novo_usuario(nome: str) -> Usuario:
    """
    cria um usuario para *nome*

    exemplos:
    >>> cria_novo_usuario('Neymar')
    Usuario(nome='Neymar', aura=0, amigos=[], depoimentos=[])
    >>> cria_novo_usuario('Miguel')
    Usuario(nome='Miguel', aura=0, amigos=[], depoimentos=[])
    >>> cria_novo_usuario('Loiro')
    Usuario(nome='Loiro', aura=0, amigos=[], depoimentos=[])

    """
    aura = 0
    amigos = []
    depoimentos = []

    return Usuario(nome, aura, amigos, depoimentos)




def acha_indice_perfil(usuario: str, banco_de_dados: list[Usuario], idx: int) -> int:
    """
    devolve o indice do perfil de determinado *usuario* em um *banco_de_dados*, a partir do *idx*, devolvendo -1 caso o usuario nao existir no *banco_de_dados*

    exemplos:
    >>> banco = [
    ...     Usuario(
    ...         nome='Mateus',
    ...         aura=0,
    ...         amigos=['Pedro', 'Lucas', 'Diogo'],
    ...         depoimentos=[],
    ...     ),
    ...     Usuario(
    ...         nome='Diogo',
    ...         aura=0,
    ...         amigos=['Mateus', 'Pedro', 'Lucas', 'Yasmin'],
    ...         depoimentos=[],
    ...     ),
    ...     Usuario(nome='Pedro', aura=0, amigos=['Mateus', 'Diogo'], depoimentos=[]),
    ...     Usuario(
    ...         nome='Lucas', aura=0, amigos=['Mateus', 'Diogo', 'Gabi'], depoimentos=[]
    ...     ),
    ...     Usuario(nome='Gabi', aura=0, amigos=['Lucas', 'Yasmin'], depoimentos=[]),
    ...     Usuario(nome='Yasmin', aura=0, amigos=['Diogo', 'Gabi'], depoimentos=[]),
    ... ]
    >>> acha_indice_perfil('Mateus', banco, 0)
    0
    >>> acha_indice_perfil('Mateus', banco, 1)
    -1
    >>> acha_indice_perfil('Yasmin', banco, 0)
    5
    """

    if idx == len(banco_de_dados):
        resultado = -1

    else:
        if banco_de_dados[idx].nome == usuario:
            resultado = idx
        else:
            resultado = acha_indice_perfil(usuario, banco_de_dados, idx + 1)

    return resultado




def ja_sao_amigos(idx_usuario1: int, idx_usuario2: int, banco_de_dados: list[Usuario]) -> bool:
    """
    confere se o *usuario1* e o *usuario2*, com base no *banco_de_dados*, ja sao amigos

    exemplos
    >>> banco = [
    ...     Usuario(nome='Mateus', aura=0, amigos=['Pedro', 'Lucas', 'Diogo']),
    ...     Usuario(nome='Diogo', aura=0, amigos=['Mateus', 'Pedro', 'Lucas', 'Yasmin']),
    ...     Usuario(nome='Pedro', aura=0, amigos=['Mateus', 'Diogo']),
    ...     Usuario(nome='Lucas', aura=0, amigos=['Mateus', 'Diogo', 'Gabi']),
    ...     Usuario(nome='Gabi', aura=0, amigos=['Lucas', 'Yasmin']),
    ...     Usuario(nome='Yasmin', aura=0, amigos=['Diogo', 'Gabi']),
    ... ]
    >>> ja_sao_amigos('Mateus', 'Lucas', banco)
    True
    >>> ja_sao_amigos('Mateus', 'Yasmin', banco)
    False
    """
    sao_amigos = False
    i = 0

    for amigo in banco_de_dados[idx_usuario1].amigos:
        if amigo == banco_de_dados[idx_usuario2].nome:
            sao_amigos = True

    return sao_amigos




def coloca_por_ultimo(nome: str, lista: list[str], idx: int) -> list[str]:
    """
    troca o *nome* de lugar com o ultimo lugar da *lista*, a partir de *idx*

    exemplos:
    >>> lista = ['Mateus', 'Diogo', 'Pedro', 'Lucas']
    >>> coloca_por_ultimo('Mateus', lista, 0)
    ['Lucas', 'Diogo', 'Pedro', 'Mateus']
    >>> lista = ['Mateus']
    >>> coloca_por_ultimo('Mateus', lista, 0)
    ['Mateus']
    >>> coloca_por_ultimo('Mateus', lista, 1)
    []
    """
    if idx == len(lista):
        lista = []
    else:
        if lista[idx] == nome:
            aux = lista[idx]
            lista[idx] = lista[len(lista) - 1]
            lista[len(lista) - 1] = aux
        else:
            lista = coloca_por_ultimo(nome, lista, idx + 1)

    return lista




def busca_amizades(usuario: str, banco_de_dados: list[Usuario]) -> list[str]:
    """
    busca a lista de amizades de *usuario* em um *banco_de_dados*

    exemplos:
    >>> banco = [
    ...     Usuario(
    ...         nome='Mateus',
    ...         aura=0,
    ...         amigos=['Pedro', 'Lucas', 'Diogo'],
    ...         depoimentos=[],
    ...     ),
    ...     Usuario(
    ...         nome='Diogo',
    ...         aura=0,
    ...         amigos=['Mateus', 'Pedro', 'Lucas', 'Yasmin'],
    ...         depoimentos=[],
    ...     ),
    ...     Usuario(nome='Pedro', aura=0, amigos=['Mateus', 'Diogo'], depoimentos=[]),
    ...     Usuario(
    ...         nome='Lucas', aura=0, amigos=['Mateus', 'Diogo', 'Gabi'], depoimentos=[]
    ...     ),
    ...     Usuario(nome='Gabi', aura=0, amigos=['Lucas', 'Yasmin'], depoimentos=[]),
    ...     Usuario(nome='Yasmin', aura=0, amigos=['Diogo', 'Gabi'], depoimentos=[]),
    ... ]
    >>> busca_amizades('Yasmin', banco)
    ['Diogo', 'Gabi']
    >>> busca_amizades('Mateus', banco)
    ['Pedro', 'Lucas', 'Diogo']

    """
    achou = False
    amigos = []
    i = 0
    while i < len(banco_de_dados) and not achou:
        if banco_de_dados[i].nome == usuario:
            amigos = banco_de_dados[i].amigos
            achou = True
        else:
            i = i + 1

    return amigos




def recomendacoes_de_amizades(usuario: str, banco_de_dados: list[Usuario]) -> list[str]:
    """
    faz a lista de amigos dos amigos do *usuario* a partir dos seus amigos
    e suas amizades registradas no *banco_de_dados*

    como ordenar do maior amigo para o menor

    exemplos:
    >>> banco = [
    ...     Usuario(
    ...         nome='Mateus',
    ...         aura=0,
    ...         amigos=['Pedro', 'Lucas', 'Diogo'],
    ...         depoimentos=[],
    ...     ),
    ...     Usuario(
    ...         nome='Diogo',
    ...         aura=0,
    ...         amigos=['Mateus', 'Pedro', 'Lucas', 'Yasmin'],
    ...         depoimentos=[],
    ...     ),
    ...     Usuario(nome='Pedro', aura=0, amigos=['Mateus', 'Diogo'], depoimentos=[]),
    ...     Usuario(
    ...         nome='Lucas', aura=0, amigos=['Mateus', 'Diogo', 'Gabi'], depoimentos=[]
    ...     ),
    ...     Usuario(nome='Gabi', aura=0, amigos=['Lucas', 'Yasmin'], depoimentos=[]),
    ...     Usuario(nome='Yasmin', aura=0, amigos=['Diogo', 'Gabi'], depoimentos=[]),
    ... ]

    >>> recomendacoes_de_amizades('Gabi', banco)
    ['Mateus', 'Diogo']
    >>> recomendacoes_de_amizades('Yasmin', banco)
    ['Mateus', 'Pedro', 'Lucas']
    """
    
    recomendacoes_para_o_usuario = []
    amigos = busca_amizades(usuario, banco_de_dados)

    for amigo in amigos:
        amigos_dos_amigos = busca_amizades(amigo, banco_de_dados)
        for i in range(len(amigos_dos_amigos)):
            if (
                amigos_dos_amigos[i] != usuario
                and amigos_dos_amigos[i] not in recomendacoes_para_o_usuario and amigos_dos_amigos[i] not in amigos
            ):
                recomendacoes_para_o_usuario.append(amigos_dos_amigos[i])

    return recomendacoes_para_o_usuario




def faz_depoimento(emissor: str, destinatario: str, mensagem: str, banco_de_dados: list[Usuario]) -> None:
    """
    permite com que o *emissor* faca um depoimento(escreva uma *mensagem*) ao *destinatario*
    ambos em um *banco_de_dados*, e adicione-o no perfil do *destinatario*
    exemplos:
    >>> banco = [
    ...     Usuario(nome='Mateus', aura=0, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Pedro', aura=0, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Lucas', aura=0, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Yasmin', aura=0, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Diogo', aura=0, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Gabi', aura=0, amigos=[], depoimentos=[]),
    ... ]

    >>> faz_depoimento('Mateus', 'Pedro', 'amigo fera!', banco)

    >>> banco
    [Usuario(nome='Mateus', aura=0, amigos=[], depoimentos=[]), Usuario(nome='Pedro', aura=0, amigos=[], depoimentos=[Depoimento(emissor='Mateus', destinatario='Pedro', mensagem='amigo fera!')]), Usuario(nome='Lucas', aura=0, amigos=[], depoimentos=[]), Usuario(nome='Yasmin', aura=0, amigos=[], depoimentos=[]), Usuario(nome='Diogo', aura=0, amigos=[], depoimentos=[]), Usuario(nome='Gabi', aura=0, amigos=[], depoimentos=[])]

    >>> faz_depoimento('Gabi', 'Diogo', 'amo o Joaquim', banco) 

    >>> banco
    [Usuario(nome='Mateus', aura=0, amigos=[], depoimentos=[]), Usuario(nome='Pedro', aura=0, amigos=[], depoimentos=[Depoimento(emissor='Mateus', destinatario='Pedro', mensagem='amigo fera!')]), Usuario(nome='Lucas', aura=0, amigos=[], depoimentos=[]), Usuario(nome='Yasmin', aura=0, amigos=[], depoimentos=[]), Usuario(nome='Diogo', aura=0, amigos=[], depoimentos=[Depoimento(emissor='Gabi', destinatario='Diogo', mensagem='amo o Joaquim')]), Usuario(nome='Gabi', aura=0, amigos=[], depoimentos=[])]

    """
    tipo_depoimento = Depoimento(emissor, destinatario, mensagem)

    for usuario in banco_de_dados:
        if usuario.nome == destinatario:
            usuario.depoimentos.append(tipo_depoimento)
            trata_aura(Aura.RECEBER_DEPOIMENTO, usuario, banco_de_dados)
        if usuario.nome == emissor:
            trata_aura(Aura.FAZER_DEPOIMENTO, usuario, banco_de_dados)




def ordena_pela_aura(banco_de_dados: list[Usuario]) -> None:
    """
    ordena o *banco_de_dados* de usuarios pela sua aura, da maior para a menor,
    e se caso de mesma aura, ordenando pela ordem alfabetica

    exemplos:
    >>> banco = [
    ...     Usuario(nome='Mateus', aura=1000, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Pedro', aura=150, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Lucas', aura=150, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Yasmin', aura=300, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Diogo', aura=200, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Gabi', aura=100, amigos=[], depoimentos=[]),
    ... ]
    >>> ordena_pela_aura(banco)
    >>> banco
    [Usuario(nome='Mateus', aura=1000, amigos=[], depoimentos=[]), Usuario(nome='Yasmin', aura=300, amigos=[], depoimentos=[]), Usuario(nome='Diogo', aura=200, amigos=[], depoimentos=[]), Usuario(nome='Lucas', aura=150, amigos=[], depoimentos=[]), Usuario(nome='Pedro', aura=150, amigos=[], depoimentos=[]), Usuario(nome='Gabi', aura=100, amigos=[], depoimentos=[])]
    """
    for i in range(len(banco_de_dados)):
        j = i
        while j > 0 and banco_de_dados[j - 1].aura <= banco_de_dados[j].aura:
            if banco_de_dados[j].aura == banco_de_dados[j - 1].aura:
                if banco_de_dados[j].nome < banco_de_dados[j - 1].nome:
                    aux = banco_de_dados[j]
                    banco_de_dados[j] = banco_de_dados[j - 1]
                    banco_de_dados[j - 1] = aux

            else:
                aux = banco_de_dados[j]
                banco_de_dados[j] = banco_de_dados[j - 1]
                banco_de_dados[j - 1] = aux

            j = j - 1




def adiciona_usuario(usuario: Usuario, banco_de_dados: list[Usuario]) -> None:
    """
    adiciona determinado *usuario* em um *banco_de_dados* de usuarios

    exemplos:
    >>> banco = [
    ...     Usuario(nome='Mateus', aura=1000, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Pedro', aura=150, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Lucas', aura=150, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Yasmin', aura=300, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Diogo', aura=200, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Gabi', aura=100, amigos=[], depoimentos=[]),
    ... ]
    >>> adiciona_usuario(
    ...     Usuario(nome='Neymar', aura=670, amigos=[], depoimentos=[]), banco
    ... )
    >>> banco
    [Usuario(nome='Mateus', aura=1000, amigos=[], depoimentos=[]), Usuario(nome='Pedro', aura=150, amigos=[], depoimentos=[]), Usuario(nome='Lucas', aura=150, amigos=[], depoimentos=[]), Usuario(nome='Yasmin', aura=300, amigos=[], depoimentos=[]), Usuario(nome='Diogo', aura=200, amigos=[], depoimentos=[]), Usuario(nome='Gabi', aura=100, amigos=[], depoimentos=[]), Usuario(nome='Neymar', aura=670, amigos=[], depoimentos=[])]
    """
    
    usuario_ja_existe = existe_usuario(usuario.nome, banco_de_dados)

    if not usuario_ja_existe:
        banco_de_dados.append(usuario)




def trata_aura(acao: Aura, usuario: Usuario, banco_de_dados: list[Usuario]) -> None:
    '''
    concede aura ou retiura aura de um *usuario*, de um *banco_de_dados* com base em sua *acao*

    exemplos: 
    >>> banco = [Usuario(nome='Mateus', aura=1000, amigos=[], depoimentos=[])]
    >>> trata_aura(Acao.FAZER_DEPOIMENTO, Usuario(nome='Mateus', aura=1000, amigos=[], depoimentos=[]),banco)
    >>> banco
    [Usuario(nome='Mateus', aura=1050, amigos=[], depoimentos=[])]
    >>> trata_aura(Acao.RECEBER_DEPOIMENTO, Usuario(nome='Mateus', aura=1050, amigos=[], depoimentos=[]),banco)
    >>> banco
    [Usuario(nome='Mateus', aura=1250, amigos=[], depoimentos=[])]
    >>> trata_aura(Acao.FAZER_AMIZADE, Usuario(nome='Mateus', aura=1250, amigos=[], depoimentos=[]), banco)
    >>> banco
    [Usuario(nome='Mateus', aura=1350, amigos=[], depoimentos=[])]
    >>> trata_aura(Acao.DESFAZER_AMIZADE, Usuario(nome='Mateus', aura=1350, amigos=[], depoimentos=[]), banco)
    >>> banco
    [Usuario(nome='Mateus', aura=1200, amigos=[], depoimentos=[])]

    '''
    for perfil in banco_de_dados:
        if perfil == usuario:
            if acao == Aura.FAZER_DEPOIMENTO:
                perfil.aura = perfil.aura + 50
            elif acao == Aura.RECEBER_DEPOIMENTO:
                perfil.aura = perfil.aura + 200
            elif acao == Aura.FAZER_AMIZADE:
                perfil.aura = perfil.aura + 100
            elif acao == Aura.DESFAZER_AMIZADE:
                perfil.aura = perfil.aura - 150




def cria_amizade(amigo1: Usuario, amigo2: Usuario, banco_de_dados: list[Usuario]) -> None:
    '''
    cria a amizade entre *amigo1* e o *amigo2*, estando eles registrados em um *banco_de_dados*

    exemplos:
    >>> banco = [Usuario(nome='Mateus', aura=1000, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Pedro', aura=150, amigos=[], depoimentos=[])]

    >>> cria_amizade(Usuario(nome='Mateus', aura=1000, amigos=[], depoimentos=[]), Usuario(nome='Pedro', aura=150, amigos=[], depoimentos=[]), banco)

    >>> banco
    [Usuario(nome='Mateus', aura=1000, amigos=['Pedro'], depoimentos=[]),
    ...     Usuario(nome='Pedro', aura=150, amigos=['Mateus'], depoimentos=[])]
    
    '''
    for usuario in banco_de_dados:
        if usuario == amigo1:
            usuario.amigos.append(amigo2.nome)
            trata_aura(Aura.FAZER_AMIZADE, usuario, banco_de_dados)
        elif usuario == amigo2:
            usuario.amigos.append(amigo1.nome)
            trata_aura(Aura.FAZER_AMIZADE, usuario, banco_de_dados)
    



def desfaz_amizade(ex_amigo1: Usuario, ex_amigo2: Usuario, banco_de_dados: list[Usuario]) -> None:
    '''
    desfaz a amizade entre *ex_amigo1* e *ex_amigo2*, alterando a relacao no *banco_de_dados*

    exemplo:
    >>> banco = [Usuario(nome='Mateus', aura=1000, amigos=['Pedro'], depoimentos=[]),
        ...     Usuario(nome='Pedro', aura=150, amigos=['Mateus'], depoimentos=[])]
    >>> desfaz_amizade(Usuario(nome='Mateus', aura=1000, amigos=['Pedro'], depoimentos=[]), Usuario(nome='Pedro', aura=150, amigos=['Mateus'], depoimentos=[]), banco)
    >>> banco = [Usuario(nome='Mateus', aura=1000, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Pedro', aura=150, amigos=[], depoimentos=[])]

    '''
    for usuario in banco_de_dados:
                
        if usuario == ex_amigo1:
            usuario.amigos = coloca_por_ultimo(ex_amigo2.nome, usuario.amigos, 0)
            usuario.amigos.pop()
            trata_aura(Aura.DESFAZER_AMIZADE, usuario, banco_de_dados)
                
        elif usuario == ex_amigo2:
            usuario.amigos = coloca_por_ultimo(ex_amigo1.nome, usuario.amigos, 0)
            usuario.amigos.pop()
            trata_aura(Aura.DESFAZER_AMIZADE, usuario, banco_de_dados)




def menu():
    '''
    imprime o menu da rede social
    '''
    print('Rede Social!!')
    print('[1] para Importar as Amizades de um Arquivo')
    print('[2] para Criar Usuário')
    print('[3] para Fazer Amizade')
    print('[4] para Desfazer Amizade')
    print('[5] para Fazer Depoimento')
    print('[6] para Mostrar Recomendações de Amizade para um Usuário')
    print('[7] para Mostrar o Ranking dos Usuários pela Aura')
    print('[8] para Mostrar todos os usuarios e suas amizades')
    print('[0] para Sair')




def imprime_usuarios(banco_de_dados: list[Usuario]):
    '''
    imprime o perfil de todos os usuarios da rede no momento

    exemplos:
    >>> banco = [
    ...     Usuario(nome='Mateus', aura=1000, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Pedro', aura=150, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Lucas', aura=150, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Yasmin', aura=300, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Diogo', aura=200, amigos=[], depoimentos=[]),
    ...     Usuario(nome='Gabi', aura=100, amigos=[], depoimentos=[]),
    ... ]
    >>> imprime_usuarios(banco)
    Usuario(nome='Mateus', aura=1000, amigos=[], depoimentos=[])
    Usuario(nome='Pedro', aura=150, amigos=[], depoimentos=[])
    Usuario(nome='Lucas', aura=150, amigos=[], depoimentos=[])
    Usuario(nome='Yasmin', aura=300, amigos=[], depoimentos=[])
    Usuario(nome='Diogo', aura=200, amigos=[], depoimentos=[])
    Usuario(nome='Gabi', aura=100, amigos=[], depoimentos=[])

    '''
    for usuario in banco_de_dados:
        print(usuario)
    print('')




def main():
    # A rede começa vazia; o operador a monta pelo menu (importando um
    # arquivo, criando usuários, etc.).
    # TODO: laço do menu, lendo a opção do operador e chamando a função
    # correspondente até que ele escolha sair
    #
    # As funções a seguir devem ser desenvolvidas e exercitadas pelo menu:
    # TODO: importar amizades de um arquivo (função 1)
    # TODO: criar usuário
    # TODO: fazer e desfazer amizade (operação 4)
    # TODO: fazer depoimento (operação 5)
    # TODO: recomendações de amizade para um usuário (função 2)
    # TODO: ranking dos usuários pela aura (função 3)
    continuar = True 
    banco_de_dados = []
    while continuar:

        menu()
        decisao = int(input('Escolha uma opção: '))
        print()

        if decisao == 0:
            print('Saindo de sua conta...')
            continuar = False
        elif decisao == 1:
            # importa as amizades de um arquivo
            arquivo_nomes = input('Cole o arquivo com as amizades desejadas: ' )
            matriz_nomes_e_amizades = le_arquivo(arquivo_nomes)
            lista_usuario = cria_lista_de_usuarios(matriz_nomes_e_amizades)

            for usuario in lista_usuario:
                adiciona_usuario(usuario, banco_de_dados)

            print('\nAmizades importadas com sucesso!!\n')
            
        elif decisao == 2:
            # cria um novo usuario
            nome = input('Digite o nome de usuario desejado: ')
            imprime_usuarios(banco_de_dados)

            if existe_usuario(nome, banco_de_dados) == True:
                print('\nEsse nome de usuario ja esta sendo utilizado!\n')

            else:
                novo_perfil = cria_novo_usuario(nome)
                adiciona_usuario(novo_perfil, banco_de_dados)
                print('\nUsuario criado com sucesso!!\n')
            
        elif decisao == 3:
            # faz uma amizade
            imprime_usuarios(banco_de_dados)

            amigo1 = input('Digite o nome do usuario que deseja fazer uma amizade: ')
            amigo2 = input('Digite o nome de quem ele quer ser amigo: ')

            idx_amigo1 = acha_indice_perfil(amigo1, banco_de_dados, 0)
            idx_amigo2 = acha_indice_perfil(amigo2, banco_de_dados, 0)

            if idx_amigo1 != -1 and idx_amigo2 != -1:

                if ja_sao_amigos(idx_amigo1, idx_amigo2, banco_de_dados) == False:

                    cria_amizade(banco_de_dados[idx_amigo1], banco_de_dados[idx_amigo2], banco_de_dados)

                    print('\nAmizade criada!!\n')

                else: 

                    print('\nOs usuarios já sao amigos!\n')
            else:

                print('\nAlgum dos usuarios que voce esta tentando fazer a amizade nao existe! \n')

        elif decisao == 4:
            # desfaz uma amizade
            imprime_usuarios(banco_de_dados)

            ex_amigo1 = input('Digite o nome do usuario que deseja desfazer uma amizade: ')
            ex_amigo2 = input('Digite o nome de quem ele nao quer mais ser amigo: ')

            idx_ex_amigo1 = acha_indice_perfil(ex_amigo1, banco_de_dados, 0)
            idx_ex_amigo2 = acha_indice_perfil(ex_amigo2, banco_de_dados, 0)
            
        
            if idx_ex_amigo1 != -1 and idx_ex_amigo2 != -1:
            
                if ja_sao_amigos(idx_ex_amigo1, idx_ex_amigo2, banco_de_dados):
                    
            
                    desfaz_amizade(banco_de_dados[idx_ex_amigo1], banco_de_dados[idx_ex_amigo2], banco_de_dados)
            
                    print('\nAmizade desfeita com sucesso!\n')
            
                else:
            
                    print('\nOs usuarios que voce esta tentado desfazer a amizade nao sao amigos!\n')
                                                
            else:
            
                print('\nAlgum dos usuarios que voce esta tentando desfazer a amizade nao existe! \n')
                
        elif decisao == 5: 
            # fazer um depoimento
            imprime_usuarios(banco_de_dados)

            emissor = input('\nQual o usuario deseja fazer um depoimento: ')
            destinatario = input('Para qual usuario destina-se o depoimento? ')

            indice_emissor = acha_indice_perfil(emissor, banco_de_dados, 0)
            indice_destinatario = acha_indice_perfil(destinatario, banco_de_dados, 0)
    
            if indice_emissor != -1 and indice_destinatario != -1:
                if ja_sao_amigos(indice_emissor, indice_destinatario, banco_de_dados):

                    mensagem = input('Gaste suas palavras fazendo essa bela declaracao! ')

                    faz_depoimento(emissor, destinatario, mensagem, banco_de_dados)
            
                    print('\nDepoimento adicionado com sucesso!!\n')
        
                else:
        
                        print('\nNao foi possivel concluir o depoimento, pois os usuarios ainda nao sao amigos!\n')
                
            else:
        
                print('\nO emissor ou o destinatario do depoimento ainda nao é um usuario registrado!\n')

        elif decisao == 6: 
            # recomendacoes de amizade para determinado usuario
            usuario_base = input('Olá, digite qual usuario deseja ver suas recomendacoes de amizades: ')

            verificacao = existe_usuario(usuario_base, banco_de_dados)

            if verificacao:
                 sugestoes_usuario_base = recomendacoes_de_amizades(usuario_base, banco_de_dados)
                 print('\nO(s) usuario(s)', sugestoes_usuario_base, 'é/são uma otima opcao de amizade para voce!\n')
                 
            else:

                print('\n O usuario que voce digitou nao existe!\n')

        elif decisao == 7:
            # imprime o ranking dos usuarios pela AURA
            ordena_pela_aura(banco_de_dados)
            imprime_usuarios(banco_de_dados)

        else:
            print('Comando errado, insira um numero entre 0 e 7! ')


        


if __name__ == '__main__':
    main()
