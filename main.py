import csv
from mergeSort import merge_sort
from  quickSort import quickSort


HEADER = "ï»¿Inventarnummer;Inventarort"
array_dict = []
def main():
    path_file = "C:\\Users\\Regis\\Desktop\\Cecile\\thema.csv"

    # lecture et transformation en dictionnaires
    with open(path_file, 'r') as csvfile:
        csv_dic_reader = csv.DictReader(csvfile)

        for row in csv_dic_reader:
            value = row[HEADER]
            inventarnummer, inventarort = value.split(";")
            #array_dict.append({inventarort: int(inventarnummer)})
            array_dict.append({"Inventarort": inventarort, "Inventarnummer": int(inventarnummer)})
        # trie du dictionnaire
        sorted_tabs1 = quickSort(array_dict)
        #sorted_tabs2 = merge_sort(array_dict)

    # creation a l'aide du dictionnaire
    with open("sorted1.csv", 'w', newline='') as file:
       writer = csv.DictWriter(file, fieldnames=["Inventarort", "Inventarnummer"])
       writer.writeheader()
       writer.writerows(sorted_tabs1)

#Appel du main
main()

#A   B

# # [ {
#     "D1" : 6565
# # [{
# #     "Inventarort": "D1"
# #     "Inventarnummer" : 586
# # }]