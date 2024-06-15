# definition
def quickSort(tabs):
    # cas de base
    if len(tabs) <= 1:
        return tabs
    # autre cas
    else:
        # tabs.pop()  == tabs[len(tabs)-1] recuperer le dernier element du tabs
        pivot = tabs.pop()
        gauche = []
        droite = []

        droite.append(pivot)

        for dic_values in tabs:

            value1 = dic_values["Inventarnummer"]
            value2 = pivot["Inventarnummer"]
            if (value1 <= value2):
                gauche.append(dic_values)
            else:
                droite.append(dic_values)
        return quickSort(gauche) + quickSort(droite)