import matplotlib.pyplot as plt   # Importa la libreria 

# Función que recibe etiquetas (nombres de columnas y valores y las grafica)
def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()  # Obtener Variables que me da la libreria matplotlib
  ax.bar(labels, values) # Genera una gráfica de barras
  plt.savefig(f"./imgs/{name}bar.png")
  plt.close

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig("chart_pie.png")
  plt.close

# Para ejecutar como un script 
if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
 # generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)