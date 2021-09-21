#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List
import time as tm

def convert_to_absolute(number: float) -> float:
    if number < 0 :
        number *= -1
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    lst_nom_complet = []
    for character in range(len(prefixes)):
        lst_nom_complet.append(prefixes[character] + suffixe)
    return lst_nom_complet

    """
    for character in prefixes:
        lst_nom_complet.append(character + suffixe)
    """


def prime_integer_summation() -> int:
    sum_prime_integer = 0
    i = 0
    nombre_premier = 2
    timer_start = tm.perf_counter()
    while (i<100):
        est_nb_premier = True
        
        for j in range(2, (int(nombre_premier/2)+1)):
         
            if nombre_premier % j == 0 and est_nb_premier:
                est_nb_premier = False
            
        if est_nb_premier:
            sum_prime_integer += nombre_premier
            i += 1
        nombre_premier += 1
    timer_end = tm.perf_counter()
    print(f"run time for prime_integer_summation : {timer_end - timer_start :0.4f} secondes ")
    
    return sum_prime_integer


def factorial(number: int) -> int:
    
    produit = 1
    while(number > 0):
        produit *= (number)
        number += -1
        
    return produit


def use_continue() -> None:
    for i in range(1, 11):
        if i == 5:
            continue
        print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    
    list_verify = []
    for groupe in groups:
        est_valide = True
        if len(groupe) > 10 or len(groupe) <= 3:
                est_valide = False
        else:
            for age_personne in groupe:
                
                if age_personne == 25 :
                    est_valide = True
                    break       
                else:
                    if age_personne < 18 :
                        est_valide = False
                    if age_personne > 70 :
                        for i in groupe:
                            if i == 50:
                                est_valide = False
           
        list_verify.append(est_valide)

    return list_verify


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
