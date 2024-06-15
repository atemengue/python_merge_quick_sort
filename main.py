from mergeSort import merge_sort
from  quickSort import quickSort
from utils.utils import read_csv_and_convert_to_dict, write_csv, menu
import time

sorted_tabs= []

def main():
    Trouve = False
    path_file = input("Entrer le chemin du fichier: ")
    start = 0
    end = 0
    # lecture et transformation en tableau de dictionnaire

    array_dict = read_csv_and_convert_to_dict(path_file)

    menu()

    while (not Trouve):
        choix = input("Choississez 1 ou 2: ")
        if choix == '1' or choix == '2':
            Trouve = True

    # trie avec le quick ou le merge
    if choix == '1':
        start = time.time()

        sorted_tabs = quickSort(array_dict)

        end = time.time()
    elif choix == '2':
        start = time.time()

        sorted_tabs = merge_sort(array_dict)

        end = time.time()

    # creation du fichier csv trie
    write_csv(sorted_tabs)
    print(f'Time Execution:", {(end - start) * 1000} milliseconds')

#Appel du main
main()
