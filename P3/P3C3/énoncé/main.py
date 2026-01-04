# Écrivez votre code ici !

import csv

# Extraction de fichiers

def extract(file_name="input.csv"):
    data = []
    with open(file_name, "r") as file:
        csv_reader = csv.DictReader(file)
        for line in csv_reader:
            data.append(line)
    return data

#Tranformation de données

def transform(data_to_transform):
    data_to_load = []
    for data in data_to_transform:
        transformed_data = {}
        transformed_data["nom"] = data["nom"]
        transformed_data["salaire"] = int(data["heures_travaillees"]) * 15
        data_to_load.append(transformed_data)
    return data_to_load

#Charge de données

def load(data_to_load, filename="output.csv"):
    with open(filename, mode="w") as file:
        fieldnames = ["nom", "salaire"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for data in data_to_load:
            writer.writerow(data)


def main():
    data_to_transform = extract("input.csv")
    data_to_load = transform(data_to_transform)
    load(data_to_load, "output.csv")


if __name__ == "__main__":
    main()
    
# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()
