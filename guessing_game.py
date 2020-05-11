"""
Le script suivant est un programme du jeu du Plus ou Moins.
Le but étant de choisir un nombre entre 0 et 10 000,
et de le faire deviner à l'ordinateur en répondant à chaque tour
"plus" ou "moins" pour guider l'ordinateur
afin qu'il puisse déterminer le nombre.

Le code utilise une approche fonctionnelle et déclarative.
"""

# Constante utilisée pour récupérer les labels
# que peut rentrer l'utilisateur pour guider l'ordinateur
poss = {
    'high': ['plus', '+', 'higher', 'high'],
    'low': ['moins', '-', 'lower', 'low'],
    'eq': ['bravo', 'egal', '=', 'equal', 'eq'],
}

def disp_poss(poss: [str]) -> str:
    """
    Fonction utilitaire qui permet de retourner le texte à afficher
    pour présenter les différents labels,
    pour que l'utilisateur guide l'ordinateur.

    Elle prend en paramètre une list de chaines de caractères,
    représentant les labels.
    """
    return ' ou '.join(map(lambda p: '"{}",'.format(p), poss))

def ask() -> str:
    """
    Fonction qui permet de récupérer la saisie de l'utilisateur
    sous forme de chaine de caractère, puis la retourne.
    """
    print('\nEntrez :')
    print('- {} si le nombre auquel vous pensez est plus grand'
          .format(disp_poss(poss['high'])))
    print('- {} si le nombre auquel vous pensez est plus petit'
          .format(disp_poss(poss['low'])))
    print('- {} si le nombre deviné par l\'ordinateur est correct'
          .format(disp_poss(poss['eq'])))
    # On empêche l'utilisateur de rentrer une saisie incorrecte.
    while True:
        # On retire les espaces et on met la saisie en minuscule,
        # pour que la comparaison avec les labels reste valide.
        res = input('> ').strip().lower()
        if res in poss['high'] \
                or res in poss['low'] \
                or res in poss['eq']:
            break
    return res

def guess(rng: (int, int)) -> int:
    """
    Fonction qui retourne le milieu d'une intervalle `rng`
    passée en paramètre.
    """
    min, max = rng
    return (min + max) // 2

"""
`higher` et `lower` sont deux fonctions
qui prennent en paramètre
un tuple qui représente l'intervalle de nombre
dans lequel se trouve le nombre correct.
"""
def higher(rng: (int, int)) -> (int, int):
    max = rng[1]
    # Dans le cas où le nombre correct
    # est supérieur au nombre deviné par l'ordinateur
    # autrement dit `guess(rng)`,
    # alors le nombre correct appartient à l'intervalle :
    # ]guess(rng); max]
    # où `max` représente le maximum de l'intervalle précédent.
    return (guess(rng), max)

def lower(rng: (int, int)) -> (int, int):
    min = rng[0]
    # Dans le cas où le nombre correct
    # est inférieur à `guess(rng)`,
    # alors le nombre correct appartient à l'intervalle :
    # [min; guess(rng)[
    # où `min` représente le minimum de l'intervalle précédent.
    return (min, guess(rng))

def update(res: str, rng: (int, int)) -> (int, int):
    """
    Fonction qui retourne un nouveau tuple
    représentant l'intervalle de nombres
    qui contient le nombre correct.
    Cette instance dépend :
    - de la réponse de l'utilisateur
      entrée en paramètre (`res`) ;
    - et de l'intervalle précédent (`rng`)
      pour pouvoir en déduire le suivant.
    """
    if res in poss['high']:
        return higher(rng)
    elif res in poss['low']:
        return lower(rng)
    else:
        # Dans le cas où le nombre deviné par l'ordinateur
        # est égal au nombre correct,
        # alors on renvoit l'intervalle :
        # [computer.guessed; computer.guessed]
        # de sorte à récupérer la valeur trouvée
        # avec guess(rng) plus tard.
        g = guess(rng)
        return (g,)*2

def game_loop(rng) -> int:
    """
    Fonction qui renvoit le nombre correct final
    trouvé par l'ordinateur.
    
    Elle prend en paramètre un tuple qui représente
    l'intervalle de nombres qui contient
    le nombre correct.
    
    C'est une fonction qui utilise la récursivité
    pour former une boucle de jeu.
    """
    if rng[0] == rng[1]:
        return guess(rng)
    else:
        print('L\'ordinateur a deviné :', guess(rng))
        res = ask()
        return game_loop(update(res, rng))

def title(rng: (int, int)):
    """
    Fonction qui permet d'afficher le texte
    au début de la partie.
    Elle dépend de `rng`, qui est le tuple
    qui représente l'intervalle de nombre
    qui contient le nombre correct.
    """
    min, max = rng
    print('Jeu du plus ou moins')
    print('====================')
    print('Choisissez un nombre entre {} et {}'.format(min, max-1));
    print('L\'ordinateur devra deviner le nombre auquel vous pensez')
    print('Notez donc bien ce nombre.')
    print('Appuyez sur Entrée pour commencer le jeu')
    input()

def main():
    """
    Fonction principale,
    qui fait donc office de point d'entrée
    """
    # Le tuple initial qui représente l'intervalle de nombres
    # qui contiendra le nombre correct.
    # À chaque tour, sa taille diminuera pour donner
    # une meilleure précision à l'ordinateur.
    init_rng = (0, 10001)
    title(init_rng)
    result = game_loop(init_rng)
    print('L\'ordinateur a gagné encore une fois!')
    print('Le nombre auquel vous pensiez était donc :', result)

if __name__ == '__main__':
    main()
