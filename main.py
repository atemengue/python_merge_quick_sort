from mergeSort import merge_sort
from  quickSort import quickSort
from utils.utils import read_csv_and_convert_to_dict, write_csv

sorted_tabs= []

def main():
    path_file = "C:\\Users\\Regis\\Desktop\\Cecile\\thema.csv"

    print("-----------Algorithme de tri  ---------")
    print("Choississez votre algorithme")
    print("Tapez 1: Quick Sort")
    print("Tapez 2: Merge Sort")

    choix = input("Faites votre choix: ")

    # lecture et transformation en tableau de dictionnaire
    array_dict = read_csv_and_convert_to_dict(path_file)

    # trie avec le quick ou le merge
    if choix == '1':
        sorted_tabs = quickSort(array_dict)
    elif choix == '2':
        sorted_tabs = merge_sort(array_dict)
    else:
        print("Veuillez choisir 1 ou 2")
        return 0

    # creation du fichier csv trie
    write_csv(sorted_tabs)

#Appel du main
main()

#A   B

# # [ {
#     "D1" : 6565
# # [{
# #     "Inventarort": "D1"
# #     "Inventarnummer" : 586
# # }]