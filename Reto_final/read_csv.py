import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        header = next(reader)
        data=[]
        for row in reader:
            iterable = zip(header, row) #convierte el header con el  row y lo une en tuplas
            #print('***' * 5)
            #print(list(iterable))
            country_dict = {key: value for key, value in iterable} #genera un diccionario con diccionary convergation
            #print(country_dict)
            data.append(country_dict)
        return data

if __name__ == '__main__':
    data = read_csv('./Reto_final/data1.csv')
    print(data[0])