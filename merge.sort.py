def merge_sort(tabs):
    # cas de base
    if len(tabs) == 1:
        return tabs
    else:
        # cas general
        # partie 1: Division des tabs en deux partie
        taille_tabs = len(tabs)
        milieu = taille_tabs // 2
        tab1 = tabs[milieu:]
        tab2 = tabs[:milieu]

        # partie 2: Trie les deux tableaux
        tab1trie = merge_sort(tab1)
        tab2trie = merge_sort(tab2)
        #print(tab1.keys())
        #[[key, value]]  = tab2[0].items()

        # partie 3: Fusionner les deux tableaux
        return fusionner(tab1trie, tab2trie)


def fusionner(tab1, tab2):
    tab3 = []
    i = j = k = 0

    # trie les tableaux
    while (i < len(tab1) and j < len(tab2)):
        [[key1, value1]]  = tab1[i].items()
        [[key2, value2]]  = tab2[j].items()

        if value1 < value2:
            tab3.append(tab1[i])
            i += 1
            k += 1
        else:
            tab3.append(tab2[j])
            j = j + 1
            k = k + 1

    while (i < len(tab1)):
        tab3.append(tab1[i])
        i += 1
        k += 1
    while (j < len(tab2)):
        tab3.append(tab2[j])
        j += 1
        k += 1
    return tab3