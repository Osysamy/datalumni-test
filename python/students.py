import csv

def recoverRows(filename):
    data = []
    file=open(filename,"r")
    test=csv.reader(file)
    for row in test:
        data.append(row)
    return data

def calculateRows(data):
    i=0
    for row in data:
       i=i+1
    return i

def listDegree(name):
    list = []
    for row in name:
       list.append(row[4])
    list = set(list)
    return list
       
    


if __name__ == "__main__":

    filename = 'students.csv'
    data = recoverRows(filename)
    print(data)
    rows = data
    print(f'\nLe fichier brut contient {len(rows)} lignes')
   
    degrees = listDegree(data)
    print(f'\nLe fichier contient {len(degrees)} diplômes uniques')

    # Donnez, dans un dict, pour chaque diplôme le nombre d'étudiant
    # par catégorie d'utilisateur (student, alumni, ...)
    users_per_degree = 
    print(f'\nLa répartition des diplômes est la suivante :')
    for degree in users_per_degree.keys():
        print(f' - {degree}, {users_per_degree[degree]} étudiants')

    # Enregistrez le dictionnaire dans un nouveau fichier `degree_count.json`
    # TODO
    print(f'\nFichier `degree_count.json` enregistré !')