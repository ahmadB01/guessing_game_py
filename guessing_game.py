"""
Le script suivant est un programme du jeu du Plus ou Moins.
Le but étant de choisir un nombre dans un certain intervalle,
et de le faire deviner à l'ordinateur en répondant à chaque
tour par "plus" ou "moins" pour le guider afin qu'il puisse
déterminer le nombre
"""

# Constante utilisée pour récupérer les labels
# de chaque commande pour guider l'ordinateur
labels = {
    'high': ('plus', '+', 'higher', 'high'),
    'low': ('moins', '-', 'lower', 'low'),
    'eq': ('bravo', 'egal', '=', 'equal', 'eq'),
}

def disp_labels(cmd):
    """
    Fonction utilitaire qui permet de renvoyer la chaine
    de caractères à afficher par commande
    (cf. la constante `labels` et la fonction `ask`)
    """
    return ', ou '.join(
        map(lambda label: '"{}"'.format(label), cmd))

def ask(guess, tries):
    """
    Fonction qui permet de récupérer
    la réponse de l'utilisateur
    """
    print('L\'ordinateur a deviné :', guess)
    print('Coups :', tries, end='\n\n')
    print('* Si le nombre auquel vous pensez est plus grand, entrez:\n {}.'
          .format(disp_labels(labels['high'])))
    print('* Si le nombre auquel vous pensez est plus petit, entrez:\n {}.'
          .format(disp_labels(labels['low'])))
    print('* Sinon, entrez:\n {}.'
          .format(disp_labels(labels['eq'])))

    # On empêche l'utilisateur
    # de rentrer une valeur incorrecte
    while True:
        res = input('> ').strip().lower()
        if res in labels['high'] \
               or res in labels['low'] \
               or res in labels['eq']:
            return res

def update(res, rng, guess):
    """
    Fonction qui met à jour l'intervalle
    en fonction de la réponse de l'utilisateur
    """
    if res in labels['high']:
        return guess, rng[1]
    elif res in labels['low']:
        return rng[0], guess
    else:
        return guess, guess

def loop(rng, tries):
    """
    Fonction qui renvoit à la fin le nombre correct
    trouvé par l'ordinateur
    C'est une fonction récursive ce qui permet
    de former une boucle de jeu
    """
    if rng[0] == rng[1]:
        return rng[0], len(tries)
    else:
        guess = sum(rng) // 2
        tries.append(guess)
        res = ask(guess, tries)
        return loop(update(res, rng, guess), tries)

def title(rng):
    """
    Fonction utilitaire qui permet d'afficher le texte
    au début de la partie
    """
    print('Jeu du plus ou moins')
    print('====================')
    print('Choisissez un nombre entre {} et {}'
          .format(rng[0], rng[1]-1));
    print('L\'ordinateur devra deviner le nombre auquel vous pensez')
    print('Notez donc bien ce nombre.')
    print('Appuyez sur Entrée pour commencer le jeu')
    input()

def main():
    """
    Fonction qui fait office de point d'entrée
    du programme
    """
    init_rng = (0, 10001)
    title(init_rng)
    result, n = loop(init_rng, [])
    print('L\'ordinateur a gagné encore une fois en {} coups!'
          .format(n))
    print('Le nombre auquel vous pensiez était donc :', result)

if __name__ == '__main__':
    main()
