import csv
from mergeSort import merge_sort


HEADER = "ï»¿Inventarnummer;Inventarort"
array_dict = []
def main():
    path_file = "C:\\Users\\Regis\\Desktop\\Cecile\\thema.csv"

    with open(path_file, 'r') as csvfile:
        csv_dic_reader = csv.DictReader(csvfile)

        for row in csv_dic_reader:
            value = row[HEADER]
            inventarort, inventarnummer = value.split(";")
            array_dict.append({inventarnummer: int(inventarort)})

#Appel du main
main()