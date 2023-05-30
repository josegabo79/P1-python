import utils
import read_csv
import charts

# Reto 2:
def run():
  # Enviamos la ubicación del archvo y recibimos el data
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)

  country = input("Digite el pais: ")
  # Le pasamos la data que esta en el diccionario y el país que queremos
  result = utils.population_by_country(data, country) 

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country["Country/Territory"], labels, values)
  
# Se utiliza para ejecutar run() cuando sea llamado directamente desde main.py
if __name__ == "__main__":
  run()

''' # Reto 1
def run():
  # Enviamos la ubicación del archvo y recibimos el data
  data = read_csv.read_csv("./app/data.csv") 
  country = input("Digite el pais: ")
  # Le pasamos la data que esta en el diccionario y el país que queremos
  result = utils.population_by_country(data, country) 

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)
''' 