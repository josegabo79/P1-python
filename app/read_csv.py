import csv # Moddulo nativo de Python para leer csv

def read_csv(path):     #Recibe la ubicación del archivo
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',') # Lector del archivo
    header = next(reader)   # Extrae el nombre de la columna que es la primera fila del archivo csv (Array de nombres)
    data = []
    for row in reader:    # Iterador para leer fila a fila 
      iterable = zip(header, row) # Une el nombre de la columna con el resto de filas y entrega un Array de tuplas      
      country_dict = {key: value for key, value in iterable} #Crea el diccionario (Dictionary comprehensions) usando la sintaxis e iterando con el for 
      data.append(country_dict)
    return data


if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])
